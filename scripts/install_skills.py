#!/usr/bin/env python3
"""Install the explicitly listed study bundle, without replacing user files."""

import argparse
from pathlib import Path
import sys

# Keep preview/check from creating local bytecode files during this import.
sys.dont_write_bytecode = True
from build_skills import manifest_data, no_symlinks, package_files, project_path


def bundle_files(selected):
    chosen, files = package_files(selected)
    distribution = project_path(manifest_data()["distribution_root"])
    for relative, expected in files.items():
        path = distribution / relative
        no_symlinks(path)
        if not path.is_file() or path.read_bytes() != expected:
            raise ValueError("Published packages are missing/stale; run build_skills.py --write first")
    return chosen, chosen, files


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
        print(f"Skills: {', '.join(chosen)}; each includes references and license")
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
