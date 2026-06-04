#!/usr/bin/env python3
"""
Validate Royalty OS example YAML files against JSON Schema files.

Required Python packages:

* PyYAML
* jsonschema

Install:
pip install pyyaml jsonschema

Usage:
python scripts/validate_examples.py
"""

import json
import sys
from pathlib import Path

try:
import yaml
except ImportError as exc:
print("Missing dependency: PyYAML")
print("Install with: pip install pyyaml")
raise SystemExit(1) from exc

try:
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError
except ImportError as exc:
print("Missing dependency: jsonschema")
print("Install with: pip install jsonschema")
raise SystemExit(1) from exc

REPO_ROOT = Path(**file**).resolve().parents[1]

VALIDATION_TARGETS = [
{
"name": "Royalty OS Value Circulation Example",
"example": REPO_ROOT / "examples" / "value-circulation.example.yaml",
"schema": REPO_ROOT / "schemas" / "royalty-os.schema.json",
}
]

def load_yaml(path: Path) -> object:
"""Load a YAML file."""
try:
with path.open("r", encoding="utf-8") as file:
return yaml.safe_load(file)
except FileNotFoundError:
raise RuntimeError(f"YAML file not found: {path}") from None
except yaml.YAMLError as exc:
raise RuntimeError(f"Invalid YAML in {path}: {exc}") from exc

def load_json(path: Path) -> object:
"""Load a JSON file."""
try:
with path.open("r", encoding="utf-8") as file:
return json.load(file)
except FileNotFoundError:
raise RuntimeError(f"JSON Schema file not found: {path}") from None
except json.JSONDecodeError as exc:
raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc

def format_error_path(error) -> str:
"""Return a readable JSON path for a validation error."""
if not error.path:
return "<root>"

```
parts = []
for part in error.path:
    if isinstance(part, int):
        parts.append(f"[{part}]")
    else:
        if parts:
            parts.append(f".{part}")
        else:
            parts.append(str(part))

return "".join(parts)
```

def validate_target(name: str, example_path: Path, schema_path: Path) -> bool:
"""Validate one YAML example against one JSON Schema."""
print(f"Validating target: {name}")
print(f"Example: {example_path.relative_to(REPO_ROOT)}")
print(f"Schema: {schema_path.relative_to(REPO_ROOT)}")

```
data = load_yaml(example_path)
schema = load_json(schema_path)

try:
    Draft202012Validator.check_schema(schema)
except SchemaError as exc:
    raise RuntimeError(f"Invalid JSON Schema in {schema_path}: {exc}") from exc

validator = Draft202012Validator(
    schema,
    format_checker=FormatChecker(),
)

errors = sorted(
    validator.iter_errors(data),
    key=lambda error: list(error.path),
)

if errors:
    print("")
    print("Validation failed.")
    for error in errors:
        print(f"- Path: {format_error_path(error)}")
        print(f"  Error: {error.message}")
    print("")
    return False

print("Validation passed.")
print("")
return True
```

def main() -> int:
"""Run all validations."""
all_passed = True

```
for target in VALIDATION_TARGETS:
    try:
        passed = validate_target(
            name=target["name"],
            example_path=target["example"],
            schema_path=target["schema"],
        )
        all_passed = all_passed and passed
    except RuntimeError as exc:
        print("")
        print("Validation failed.")
        print(exc)
        print("")
        all_passed = False

if not all_passed:
    return 1

print("All validations passed.")
return 0
```

if **name** == "**main**":
raise SystemExit(main())
