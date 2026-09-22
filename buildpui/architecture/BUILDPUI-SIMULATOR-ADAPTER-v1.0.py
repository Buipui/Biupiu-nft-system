"""BuildPui schema adapter for the architecture simulator prototype.

The adapter validates the canonical BuildPui envelope before simulation use.
It does not perform structural, fire, durability, regulatory, or physical validation.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "buildpui/architecture/BUILDPUI-ARCHITECTURE-SCHEMA-v1.0.schema.json"


class BuildPuiSchemaError(ValueError):
    """Raised when a BuildPui object violates the canonical schema."""


class BuildPuiSchemaAdapter:
    def __init__(self, schema_path: Path = SCHEMA_PATH) -> None:
        self.schema = json.loads(schema_path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(self.schema)
        self.validator = Draft202012Validator(
            self.schema, format_checker=FormatChecker()
        )

    def validate_object(self, obj: Mapping[str, Any]) -> dict[str, Any]:
        errors = sorted(self.validator.iter_errors(obj), key=lambda e: list(e.path))
        if errors:
            details = "; ".join(
                f"{'.'.join(map(str, e.path)) or '<root>'}: {e.message}"
                for e in errors
            )
            raise BuildPuiSchemaError(details)
        return dict(obj)

    @staticmethod
    def simulation_permission(obj: Mapping[str, Any]) -> bool:
        """Allow simulation preparation only after the explicit SIMULATION-READY state."""
        return obj.get("evidence_state") == "SIMULATION-READY"

    @staticmethod
    def engineering_validation_allowed(obj: Mapping[str, Any]) -> bool:
        """Schema validation never grants engineering validation authority."""
        return False
