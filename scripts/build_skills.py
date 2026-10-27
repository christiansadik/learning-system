#!/usr/bin/env python3
"""Generate self-contained Agent Skills from the canonical authoring files."""

import argparse
import hashlib
import json
from pathlib import Path
import posixpath
import re
import sys
import tempfile


ROOT = Path(__file__).resolve().parent.parent
RECEIPT = ".build-manifest.json"


def no_symlinks(path):
    for item in (path, *path.parents):
        if item.is_symlink():
            raise ValueError(f"Symlinked path is not a build/copy path: {item}")


def project_path(relative):
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError(f"Unsafe manifest path: {relative}")
    result = ROOT / path
    no_symlinks(result)
    if not result.resolve().is_relative_to(ROOT):
        raise ValueError(f"Path escapes checkout: {relative}")
    return result


def manifest_data():
    data = json.loads((ROOT / "skill-bundle.json").read_text(encoding="utf-8"))
    if data["format_version"] != 2 or data["distribution_root"] != "skills":
        raise ValueError("Unsupported bundle format or distribution root")
    names = data["skills"]
    if not names or len(names) != len(set(names)):
        raise ValueError("Skills must be nonempty and unique")
    if any(not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) for name in names):
        raise ValueError("Invalid skill name")
    references = data["reference_files"]
    if len(references) != len(set(references)):
        raise ValueError("Duplicate reference files")
    for name in references:
        if Path(name).name != name or Path(name).suffix not in (".md", ".json") or name == "SKILL.md":
            raise ValueError(f"Unsafe reference filename: {name}")
    if not re.fullmatch(r"[A-Za-z0-9.-]+", data["license"]):
        raise ValueError("Invalid license identifier")
    return data


def validate_links(files):
    for relative, content in files.items():
        if relative.suffix != ".md":
            continue
        for target in re.findall(r"\]\(([^)]+)\)", content.decode("utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            joined = Path(posixpath.normpath((relative.parent / target).as_posix()))
            if Path(target).is_absolute() or joined.parts[0] != relative.parts[0] or joined not in files:
                raise ValueError(f"Reference escapes its skill or is missing: {relative}: {target}")


def package_files(selected=()):
    data = manifest_data()
    unknown = set(selected) - set(data["skills"])
    if unknown:
        raise ValueError(f"Unknown skills: {', '.join(sorted(unknown))}")
    chosen = [name for name in data["skills"] if not selected or name in selected]
    source = project_path(data["source_root"])
    reference_root = project_path(data["reference_root"])
    license_bytes = project_path("LICENSE").read_bytes()
    references = {}
    actual_references = set()
    for path in reference_root.rglob("*"):
        no_symlinks(path)
        if path.is_file():
            actual_references.add(path.relative_to(reference_root).as_posix())
    if actual_references != set(data["reference_files"]):
        raise ValueError("Canonical references differ from the explicit manifest")
    for name in data["reference_files"]:
        references[name] = (reference_root / name).read_bytes()
    files = {}
    for name in chosen:
        path = source / f"{name}.md"
        no_symlinks(path)
        text = path.read_text(encoding="utf-8")
        match = re.fullmatch(r"---\n(.*?)\n---\n(.*)", text, re.DOTALL)
        if not match or f"name: {name}\n" not in match.group(1) + "\n" or "description: " not in match.group(1):
            raise ValueError(f"Missing or inconsistent skill frontmatter: {name}")
        metadata, body = match.groups()
        if re.search(r"^license:", metadata, re.MULTILINE):
            raise ValueError("Declare the distribution license only in skill-bundle.json")
        body = re.sub(r"\]\(\.\./references/([^)]+)\)", r"](references/\1)", body)
        header = "<!-- Generated from authoring; run python3 scripts/build_skills.py --write after source changes. -->\n"
        rendered = f"---\n{metadata}\nlicense: {data['license']}\n---\n{header}{body}"
        files[Path(name) / "SKILL.md"] = rendered.encode("utf-8")
        files[Path(name) / "LICENSE"] = license_bytes
        for reference, content in references.items():
            files[Path(name) / "references" / reference] = content
    validate_links(files)
    return chosen, files


def digest(content):
    return hashlib.sha256(content).hexdigest()


def atomic_write(path, content):
    no_symlinks(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    no_symlinks(path)
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".skill-build-", delete=False) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Create/update unchanged generated files")
    mode.add_argument("--check", action="store_true", help="Read-only check for a reproducible distribution")
    args = parser.parse_args()
    try:
        chosen, files = package_files()
        destination = project_path(manifest_data()["distribution_root"])
        if destination.exists() and not destination.is_dir():
            raise ValueError("Distribution root is not a directory")
        receipt_path = destination / RECEIPT
        no_symlinks(receipt_path)
        previous = {}
        if receipt_path.exists():
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            if receipt["format_version"] != 1:
                raise ValueError("Unknown build receipt version")
            previous = receipt["files"]
            if not isinstance(previous, dict) or any(
                not isinstance(key, str) or not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value)
                for key, value in previous.items()
            ):
                raise ValueError("Invalid generated-file hashes in build receipt")
        expected = {path.as_posix(): digest(content) for path, content in files.items()}
        obsolete = set(previous) - set(expected)
        if obsolete:
            raise ValueError(f"Obsolete generated paths require explicit review: {sorted(obsolete)}")
        if destination.exists():
            for path in destination.rglob("*"):
                no_symlinks(path)
                if path.is_file() and path != receipt_path and path.relative_to(destination) not in files:
                    raise ValueError(f"Unexpected distribution file; preserve it before rebuilding: {path}")
        changed = []
        for relative, content in files.items():
            path = destination / relative
            no_symlinks(path)
            if path.exists():
                current = path.read_bytes()
                if current == content:
                    continue
                if digest(current) != previous.get(relative.as_posix()):
                    raise ValueError(f"Edited/unrecognized generated file; nothing overwritten: {path}")
            changed.append(relative)
        receipt_bytes = (json.dumps({"format_version": 1, "files": expected}, indent=2, sort_keys=True) + "\n").encode("utf-8")
        receipt_matches = receipt_path.exists() and receipt_path.read_bytes() == receipt_bytes
        if args.check:
            if changed or not receipt_matches:
                raise ValueError("Distribution is missing/stale; preview and run --write")
            print(f"Verified {len(chosen)} self-contained skills and {len(files)} reproducible package files.")
        elif args.write:
            for relative in changed:
                path = destination / relative
                if path.exists() and digest(path.read_bytes()) != previous.get(relative.as_posix()):
                    raise ValueError(f"Generated file changed during build: {path}")
                atomic_write(path, files[relative])
            if not receipt_matches:
                atomic_write(receipt_path, receipt_bytes)
            print(f"Generated {len(chosen)} skills; wrote {len(changed)} package files and refreshed build metadata.")
        else:
            print(f"Preview: {len(changed)} of {len(files)} package files need generation; no writes performed.")
    except (OSError, ValueError, KeyError) as error:
        print(f"Build stopped: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
