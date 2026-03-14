# Changelog

All notable changes to **fieldtheory** are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [0.1.0] – 2026-03-14

### Added

- **Harmonic Lagrangian** `L = S_A·S_V/(S_A + S_V) − (1 + δ)/t²` encoding the S∝A/S∝V duality balance with a depth-weighted collapse potential.
- **Symbolic Euler-Lagrange derivation** via SymPy (`derive_lagrangian()`), treating S(t) as the primary dynamical field.
- **Numerical field simulation** (`simulate_field()`) with configurable steps, threshold, and golden-ratio defaults (S_V = φ ≈ 1.618).
- **CLI** (`ft`) with three commands:
  - `ft simulate` — run the unified field simulation
  - `ft lagrangian` — display the symbolic Euler-Lagrange equation
  - `ft version` — show the package version
- **Optional GenesisAeon stack integration** (`pip install "fieldtheory[stack]"`):
  - `medium-modulation` — modulated entropy computation
  - `cosmic-moment` — collapse-event detection
  - `entropy-governance` — duality factor
  - `entropy-table` — result export
  - `implosive-genesis` — genesis engine
  - All integrations degrade gracefully; the standalone core runs without any stack package.
- **`FieldtheoryBridge`** — exports simulation results to `entropy-table` format (falls back to plain YAML when the package is absent).
- **27 tests**, **88% coverage**, ruff-clean, mkdocs documentation.

### Architecture

```
fieldtheory/
├── core.py                  # Lagrangian, EL derivation, simulation
├── cli.py                   # ft simulate / ft lagrangian / ft version
└── entropy_table_bridge.py  # Export bridge (optional stack dep)
```

---

*This is the initial public release — the mathematical heart of the GenesisAeon stack.*
