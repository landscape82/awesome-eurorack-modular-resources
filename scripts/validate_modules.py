#!/usr/bin/env python3
"""Validate data/modules.yaml against docs/schema.md's required/recommended fields.

Exit code 1 on any required-field violation or invalid `type` value.
Recommended-field gaps and unreachable-looking URLs are warnings only.
"""
import sys
import urllib.parse
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ["manufacturer", "module", "repository", "type"]
RECOMMENDED = ["description", "platform", "build", "flash", "hardware", "license", "status"]


def load_valid_types() -> set[str]:
    tags = yaml.safe_load((ROOT / "data" / "tags.yaml").read_text())
    return {t["id"] for t in tags["types"]}


def load_known_manufacturers() -> set[str]:
    data = yaml.safe_load((ROOT / "data" / "manufacturers.yaml").read_text())
    return {m["name"] for m in data["manufacturers"]}


def validate() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    data = yaml.safe_load((ROOT / "data" / "modules.yaml").read_text())
    modules = data.get("modules", [])
    valid_types = load_valid_types()
    known_manufacturers = load_known_manufacturers()

    for i, m in enumerate(modules):
        label = f"modules[{i}] ({m.get('manufacturer', '?')} / {m.get('module', '?')})"

        for field in REQUIRED:
            if not m.get(field):
                errors.append(f"{label}: missing required field '{field}'")

        manufacturer = m.get("manufacturer")
        if manufacturer and manufacturer not in known_manufacturers:
            errors.append(
                f"{label}: manufacturer '{manufacturer}' not found in data/manufacturers.yaml "
                "(add it there, or fix a naming mismatch)"
            )

        for field in RECOMMENDED:
            if not m.get(field):
                warnings.append(f"{label}: missing recommended field '{field}'")

        repo = m.get("repository", "")
        if repo:
            parsed = urllib.parse.urlparse(repo)
            if parsed.scheme != "https" or not parsed.netloc:
                errors.append(f"{label}: repository '{repo}' is not a well-formed https:// URL")

        for t in m.get("type", []):
            if t not in valid_types:
                errors.append(f"{label}: unknown type '{t}' (see data/tags.yaml)")

    return errors, warnings


def main() -> int:
    errors, warnings = validate()

    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")

    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s).")
        return 1

    print(f"OK — {len(warnings)} warning(s), 0 errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
