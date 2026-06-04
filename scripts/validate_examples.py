#!/usr/bin/env python3
"""
Validate Royalty OS v0.2 example YAML files against modular JSON Schema files.
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

# -----------------------------
# Dependencies
# -----------------------------
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

# -----------------------------
# Paths
# -----------------------------
REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = REPO_ROOT / "schemas"
EXAMPLE_DIR = REPO_ROOT / "examples"

# -----------------------------
# Validation Targets
# -----------------------------
VALIDATION_TARGETS = [
    {
        "name": "Origin Record Example",
        "example": EXAMPLE_DIR / "origin-record.example.yaml",
        "schema": SCHEMA_DIR / "origin.schema.json",
    },
    {
        "name": "Trace Record Example",
        "example": EXAMPLE_DIR / "trace-record.example.yaml",
        "schema": SCHEMA_DIR / "trace.schema.json",
    },
    {
        "name": "Review Record Example",
        "example": EXAMPLE_DIR / "review-record.example.yaml",
        "schema": SCHEMA_DIR / "review.schema.json",
    },
    {
        "name": "Allocation Decision Example",
        "example": EXAMPLE_DIR / "allocation-decision.example.yaml",
        "schema": SCHEMA_DIR / "allocation.schema.json",
    },
    {
        "name": "Return Record Example",
        "example": EXAMPLE_DIR / "return-record.example.yaml",
        "schema": SCHEMA_DIR / "return.schema.json",
    },
]

# -----------------------------
# YAML / JSON Loaders
# -----------------------------
def load_yaml(path: Path) -> Any:
    """Load a YAML file."""
    try:
        with path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise RuntimeError(f"YAML file not found: {path}") from None
    except yaml.YAMLError as exc:
        raise RuntimeError(f"Invalid YAML in {path}: {exc}") from exc


def load_json(path: Path) -> Dict[str, Any]:
    """Load a JSON file."""
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise RuntimeError(f"JSON Schema file not found: {path}") from None
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc

# -----------------------------
# Error Path Formatter
# -----------------------------
def format_error_path(error: Any) -> str:
    """Return a readable JSON path for a validation error."""
    if not error.path:
        return "<root>"

    parts: List[str] = []
    for part in error.path:
        if isinstance(part, int):
            parts.append(f"[{part}]")
        else:
            if parts:
                parts.append(f".{part}")
            else:
                parts.append(str(part))

    return "".join(parts)

# -----------------------------
# Schema Validation
# -----------------------------
def validate_schema(schema_path: Path) -> Dict[str, Any]:
    """Load and validate a JSON Schema."""
    schema = load_json(schema_path)

    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise RuntimeError(f"Invalid JSON Schema in {schema_path}: {exc}") from exc

    return schema

# -----------------------------
# Data Validation
# -----------------------------
def validate_data(name: str, data: Any, schema: Dict[str, Any]) -> bool:
    """Validate data against a schema object."""
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
        print(f"Validation failed: {name}")
        for error in errors:
            print(f"- Path: {format_error_path(error)}")
            print(f"  Error: {error.message}")
        print("")
        return False

    print(f"Validation passed: {name}")
    return True

# -----------------------------
# Validate Single Target
# -----------------------------
def validate_target(name: str, example_path: Path, schema_path: Path) -> bool:
    """Validate one YAML example against one JSON Schema."""
    print(f"Validating target: {name}")
    print(f"Example: {example_path.relative_to(REPO_ROOT)}")
    print(f"Schema: {schema_path.relative_to(REPO_ROOT)}")

    data = load_yaml(example_path)
    schema = validate_schema(schema_path)

    passed = validate_data(name, data, schema)
    print("")
    return passed

# -----------------------------
# Value Event Log Validation
# -----------------------------
def validate_value_event_log() -> bool:
    """
    Validate value-event-log.example.yaml.
    """
    example_path = EXAMPLE_DIR / "value-event-log.example.yaml"
    event_schema_path = SCHEMA_DIR / "value-event.schema.json"

    print("Validating target: Value Event Log Example")
    print(f"Example: {example_path.relative_to(REPO_ROOT)}")
    print(f"Schema: {event_schema_path.relative_to(REPO_ROOT)}")

    data = load_yaml(example_path)
    event_schema = validate_schema(event_schema_path)

    required_fields = [
        "log_id",
        "origin_id",
        "trace_id",
        "append_only",
        "events",
    ]

    passed = True

    if not isinstance(data, dict):
        print("")
        print("Validation failed: Value Event Log Example")
        print("- Path: <root>")
        print("  Error: event log must be an object")
        print("")
        return False

    for field in required_fields:
        if field not in data:
            print("")
            print("Validation failed: Value Event Log Example")
            print(f"- Path: <root>")
            print(f"  Error: missing required field '{field}'")
            print("")
            passed = False

    if data.get("append_only") is not True:
        print("")
        print("Validation failed: Value Event Log Example")
        print("- Path: append_only")
        print("  Error: append_only must be true")
        print("")
        passed = False

    events = data.get("events")

    if not isinstance(events, list) or not events:
        print("")
        print("Validation failed: Value Event Log Example")
        print("- Path: events")
        print("  Error: events must be a non-empty list")
        print("")
        return False

    event_ids = set()

    for index, event in enumerate(events):
        event_name = f"Value Event Log Event {index + 1}"

        event_id = event.get("event_id") if isinstance(event, dict) else None
        if event_id in event_ids:
            print("")
            print(f"Validation failed: {event_name}")
            print(f"- Path: events[{index}].event_id")
            print(f"  Error: duplicate event_id '{event_id}'")
            print("")
            passed = False
        elif event_id:
            event_ids.add(event_id)

        event_passed = validate_data(event_name, event, event_schema)
        passed = passed and event_passed

    print("")

    if passed:
        print("Validation passed: Value Event Log Example")
        print("")

    return passed

# -----------------------------
# Cross-file Consistency
# -----------------------------
def validate_cross_references() -> bool:
    """
    Perform lightweight cross-file consistency checks.
    """
    print("Validating cross-file consistency...")

    origin = load_yaml(EXAMPLE_DIR / "origin-record.example.yaml")
    trace = load_yaml(EXAMPLE_DIR / "trace-record.example.yaml")
    event_log = load_yaml(EXAMPLE_DIR / "value-event-log.example.yaml")
    review = load_yaml(EXAMPLE_DIR / "review-record.example.yaml")
    allocation = load_yaml(EXAMPLE_DIR / "allocation-decision.example.yaml")
    return_record = load_yaml(EXAMPLE_DIR / "return-record.example.yaml")

    passed = True

    origin_id = origin.get("origin_id")
    trace_id = trace.get("trace_id")

    checks: List[Tuple[str, Any, Any]] = [
        ("trace.origin_id == origin.origin_id", trace.get("origin_id"), origin_id),
        ("event_log.origin_id == origin.origin_id", event_log.get("origin_id"), origin_id),
        ("event_log.trace_id == trace.trace_id", event_log.get("trace_id"), trace_id),
        ("allocation.origin_id == origin.origin_id", allocation.get("origin_id"), origin_id),
        ("allocation.trace_id == trace.trace_id", allocation.get("trace_id"), trace_id),
        ("return.origin_id == origin.origin_id", return_record.get("origin_id"), origin_id),
        ("return.trace_id == trace.trace_id", return_record.get("trace_id"), trace_id),
        ("return.allocation_id == allocation.allocation_id", return_record.get("allocation_id"), allocation.get("allocation_id")),
    ]

    for label, actual, expected in checks:
        if actual != expected:
            print(f"Cross-reference failed: {label}")
            print(f"  Expected: {expected}")
            print(f"  Actual:   {actual}")
            passed = False
        else:
            print(f"Cross-reference passed: {label}")

    event_ids = set()

    for event in event_log.get("events", []):
        if isinstance(event, dict) and "event_id" in event:
            event_ids.add(event["event_id"])

    reviewed_event_id = review.get("reviewed_event_id")
    if reviewed_event_id not in event_ids:
        print("Cross-reference failed: review.reviewed_event_id exists in event log")
        print(f"  Missing event_id: {reviewed_event_id}")
        passed = False
    else:
        print("Cross-reference passed: review.reviewed_event_id exists in event log")

    for event_id in allocation.get("based_on_events", []):
        if event_id not in event_ids:
            print("Cross-reference failed: allocation.based_on_events exists in event log")
            print(f"  Missing event_id: {event_id}")
            passed = False

    if passed:
        print("All cross-file consistency checks passed.")

    print("")
    return passed

# -----------------------------
# Main
# -----------------------------
def main() -> int:
    """Run all validations."""
    all_passed = True

    try:
        all_passed = validate_all_schemas_loadable() and all_passed
    except RuntimeError as exc:
        print("")
        print("Validation failed.")
        print(exc)
        print("")
        all_passed = False

    for target in VALIDATION_TARGETS:
        try:
            passed = validate_target(
                name=target["name"],
                example_path=target["example"],
                schema_path=target["schema"],
            )
            all_passed = passed and all_passed
        except RuntimeError as exc:
            print("")
            print("Validation failed.")
            print(exc)
            print("")
            all_passed = False

    try:
        all_passed = validate_value_event_log() and all_passed
    except RuntimeError as exc:
        print("")
        print("Validation failed.")
        print(exc)
        print("")
        all_passed = False

    try:
        all_passed = validate_cross_references() and all_passed
    except RuntimeError as exc:
        print("")
        print("Validation failed.")
        print(exc)
        print("")
        all_passed = False

    if not all_passed:
        print("One or more validations failed.")
        return 1

    print("All validations passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

