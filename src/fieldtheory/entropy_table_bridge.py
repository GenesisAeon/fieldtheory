"""Bridge between fieldtheory and the entropy-table stack package."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

try:
    from entropy_table import EntropyTable  # type: ignore[import-not-found]

    _HAS_ENTROPY_TABLE = True
except ImportError:
    _HAS_ENTROPY_TABLE = False


class FieldtheoryBridge:
    """
    Export fieldtheory simulation results to the entropy-table format.

    If the ``entropy-table`` package is installed, it is used directly.
    Otherwise, results are written as plain YAML (fully compatible schema).
    """

    def __init__(self, domain: str = "fieldtheory") -> None:
        self.domain = domain
        self._relations: dict[str, Any] = {}
        self._table: Any = None

        if _HAS_ENTROPY_TABLE:
            self._table = EntropyTable(domain=domain)

    def add_relation(self, key: str, value: float) -> None:
        """Register a named entropy relation."""
        self._relations[key] = value
        if self._table is not None:
            self._table.add_relation(key, value)

    def export(self, filepath: Path | str = "domains.yaml") -> Path:
        """
        Write relations to *filepath*.

        Delegates to EntropyTable.export() when available; falls back to
        writing a minimal YAML document otherwise.
        """
        filepath = Path(filepath)

        if self._table is not None:
            self._table.export(filepath)
            return filepath

        # Fallback: plain YAML
        payload = {"domains": {self.domain: self._relations}}
        filepath.write_text(yaml.dump(payload, default_flow_style=False), encoding="utf-8")
        return filepath
