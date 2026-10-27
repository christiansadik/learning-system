#!/usr/bin/env python3
"""Install the explicitly listed study bundle, without replacing user files."""

import argparse
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent


def no_symlinks(path):
    """Refuse redirected paths, including redirects in existing parents."""
    for item in (path, *path.parents):
        if item.is_symlink():
            raise ValueError(f"Symlinked path is not a copy destination/source: {item}")


def bundle_files(selected):
    manifest = json.loads((ROOT / "skill-bundle.json").read_text(encoding="utf-8"))
    if manifest["format_version"] != 1:
        raise ValueError("Unsupported bundle manifest version")
    names = manifest["skills"]
    if len(names) != len(set(names)):
        raise ValueError("Duplicate skill names in manifest")
    unknown = set(selected) - set(names)
    if unknown:
        raise ValueError(f"Unknown skills: {', '.join(sorted(unknown))}")
    chosen = [name for name in names if not selected or name in selected]
    directories = chosen + manifest["shared_directories"]
    if any(not re.fullmatch(r"[a-z0-9_-]+", name) for name in directories):
        raise ValueError("Unsafe directory name in manifest")
    allowed_files = {Path(name) / "SKILL.md" for name in chosen}
    for name in manifest["shared_files"]:
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts or relative.parts[0] not in manifest["shared_directories"]:
            raise ValueError(f"Unsafe shared file in manifest: {name}")
        allowed_files.add(relative)
    source = ROOT / manifest["source_root"]
    if not source.resolve().is_relative_to(ROOT):
        raise ValueError("Bundle source is outside this checkout")
    no_symlinks(source)
    files = {}
    for name in directories:
        folder = source / name
        no_symlinks(folder)
        if not folder.is_dir():
            raise ValueError(f"Missing bundle directory: {name}")
        if name in chosen and not (folder / "SKILL.md").is_file():
            raise ValueError(f"Missing SKILL.md: {name}")
        for path in sorted(folder.rglob("*")):
            no_symlinks(path)
            if path.is_file():
                if path.relative_to(source) not in allowed_files:
                    raise ValueError(f"Unlisted source file; review the manifest: {path.relative_to(source)}")
                if path.suffix not in (".md", ".json"):
                    raise ValueError(f"Unexpected bundle file: {path.relative_to(source)}")
                files[path.relative_to(source)] = path.read_bytes()
    if set(files) != allowed_files:
        raise ValueError("A file listed in the bundle manifest is missing")
    license_path = ROOT / "LICENSE"
    no_symlinks(license_path)
    if files.get(Path("_study/LICENSE.md")) != license_path.read_bytes():
        raise ValueError("Bundled license must match the canonical root LICENSE")
    for relative, content in files.items():
        if relative.suffix == ".md":
            for target in re.findall(r"\]\(([^)]+)\)", content.decode("utf-8")):
                if "://" not in target:
                    resolved = (source / relative.parent / target).resolve()
                    if not resolved.is_relative_to(source.resolve()):
                        raise ValueError(f"Reference escapes bundle: {relative}: {target}")
                    if resolved.relative_to(source.resolve()) not in files:
                        raise ValueError(f"Missing required reference: {relative}: {target}")
    return chosen, directories, files


def inspect_destination(target, directories, files):
    no_symlinks(target)
    if target.exists() and not target.is_dir():
        raise ValueError(f"Destination is not a directory: {target}")
    for name in directories:
        folder = target / name
        no_symlinks(folder)
        if folder.exists() and not folder.is_dir():
            raise ValueError(f"Managed destination is not a directory: {folder}")
        if folder.exists():
            for path in folder.rglob("*"):
                no_symlinks(path)
                if path.is_file() and path.relative_to(target) not in files:
                    raise ValueError(f"Unmanaged file inside selected bundle directory: {path}")
    missing = []
    for relative, expected in files.items():
        path = target / relative
        no_symlinks(path)
        if path.exists():
            if not path.is_file() or path.read_bytes() != expected:
                raise ValueError(f"Different existing content; nothing overwritten: {path}")
        else:
            missing.append(relative)
    return missing


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, help="Explicit destination skills directory")
    parser.add_argument("--skill", action="append", default=[], help="Install only this skill (repeatable)")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true", help="Create missing bundle files; default is preview")
    mode.add_argument("--check", action="store_true", help="Read-only check that all selected files match")
    args = parser.parse_args()
    try:
        requested = Path(args.target).expanduser()
        if ".." in requested.parts:
            raise ValueError("Use a destination without parent traversal segments")
        target = requested.absolute()
        if target == Path(target.anchor):
            raise ValueError("The filesystem root is not a skills directory")
        chosen, directories, files = bundle_files(args.skill)
        missing = inspect_destination(target, directories, files)
        print(f"Target: {target}")
        print(f"Skills: {', '.join(chosen)}; shared references included")
        if args.check:
            if missing:
                raise ValueError(f"Incomplete installation: {len(missing)} files missing")
            print(f"Verified {len(files)} matching bundle files; unrelated directories untouched.")
        elif args.apply:
            for relative in missing:
                path = target / relative
                no_symlinks(path)
                path.parent.mkdir(parents=True, exist_ok=True)
                no_symlinks(path)
                with path.open("xb") as handle:
                    handle.write(files[relative])
            print(f"Created {len(missing)} files; {len(files) - len(missing)} already identical.")
        else:
            print(f"Preview: {len(missing)} files would be created; no writes performed.")
    except (OSError, ValueError, KeyError) as error:
        print(f"Installation stopped: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
