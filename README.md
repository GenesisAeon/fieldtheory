# fieldtheory

**The unifying field theory of the GenesisAeon stack.**

[![CI](https://github.com/GenesisAeon/fieldtheory/actions/workflows/ci.yml/badge.svg)](https://github.com/GenesisAeon/fieldtheory/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/badge/coverage-88%25-brightgreen)](https://github.com/GenesisAeon/fieldtheory/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/fieldtheory)](https://pypi.org/project/fieldtheory/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19025145.svg)](https://doi.org/10.5281/zenodo.19025145)

Derives the full Lagrangian from S∝A/S∝V duality, applies medium-modulation, detects cosmic-moment collapse events and exports to entropy-table.

---

## Install

```bash
pip install fieldtheory
# with full GenesisAeon stack integration:
pip install "fieldtheory[stack]"
```

## Usage

```bash
# Run the unified field simulation
ft simulate --steps 100

# Show the symbolic Euler-Lagrange equation
ft lagrangian

# Override field parameters
ft simulate --s-a 1.0 --s-v 1.618 --depth 0.5 --threshold 0.618
```

## Python API

```python
from fieldtheory.core import simulate_field, derive_lagrangian, modulated_entropy

# Numerical simulation
result = simulate_field(steps=200, threshold=0.618)
print(result["S_mod_mean"])      # mean modulated entropy
print(result["cosmic_moments"])  # number of collapse events

# Symbolic Lagrangian + Euler-Lagrange equation
eqs = derive_lagrangian()
print(eqs["lagrangian"])        # S_A*S_V/(S_A + S_V) - (delta + 1)/t**2
print(eqs["euler_lagrange"])    # d/dt(∂L/∂Ṡ) - ∂L/∂S = 0

# Entropy-table export
from fieldtheory.entropy_table_bridge import FieldtheoryBridge
bridge = FieldtheoryBridge()
bridge.add_relation("S_mod_mean", result["S_mod_mean"])
bridge.export("domains.yaml")
```

## Architecture

```
fieldtheory/
├── core.py                  # Unified Lagrangian, EL derivation, simulation
├── cli.py                   # ft simulate / ft lagrangian / ft version
└── entropy_table_bridge.py  # Export to entropy-table (optional stack dep)
```

The Lagrangian encodes the S∝A/S∝V duality:

```
L = S_A·S_V / (S_A + S_V)  −  (1 + δ) / t²
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^
    harmonic duality balance     collapse potential
```

When `medium-modulation`, `cosmic-moment`, and `entropy-governance` are installed (`pip install "fieldtheory[stack]"`), their implementations are used transparently. Without them the package falls back to internal implementations — all tests pass either way.

---

**DOI**: [10.5281/zenodo.19025145](https://doi.org/10.5281/zenodo.19025145)
**PyPI**: `pip install fieldtheory` (oder `pip install "fieldtheory[stack]"` für den vollen GenesisAeon-Stack)

Built with [SymPy](https://www.sympy.org/) · [NumPy](https://numpy.org/) · [Typer](https://typer.tiangolo.com/) · [Rich](https://rich.readthedocs.io/)
