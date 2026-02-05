#!/usr/bin/env python3
"""Validate VS Code Updates AI sidecar JSON outputs against the schema."""

from __future__ import annotations

import json
import os
from glob import glob
from typing import Any

from jsonschema import Draft202012Validator


def load_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    schema_path = os.path.join(root, "schemas", "vscode_updates_ai_analysis.schema.json")
    schema = load_json(schema_path)

    validator = Draft202012Validator(schema)

    ai_dir = os.path.join(root, "vscode-updates", "_ai")
    files = sorted(glob(os.path.join(ai_dir, "*.ai.json")))
    if not files:
        print(f"No AI sidecar files found under: {ai_dir}")
        return 1

    failures = 0
    for path in files:
        data = load_json(path)
        errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
        if errors:
            failures += 1
            print(f"INVALID: {os.path.relpath(path, root)}")
            for err in errors[:10]:
                where = "/".join(str(p) for p in err.path) or "<root>"
                print(f"  - {where}: {err.message}")

    if failures:
        print(f"\n{failures}/{len(files)} files are invalid")
        return 2

    print(f"All {len(files)} files are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
