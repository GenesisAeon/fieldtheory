# Architecture

## Module Overview

```
src/fieldtheory/
├── __init__.py              # version, author
├── core.py                  # Lagrangian, EL derivation, simulation engine
├── cli.py                   # ft CLI (Typer + Rich)
└── entropy_table_bridge.py  # entropy-table export bridge
```

## core.py

### Symbolic layer (SymPy)

The static Lagrangian is defined at module level:

```python
L = (S_A * S_V) / (S_A + S_V) - (1 + delta) / t**2
```

`derive_lagrangian()` extends this to a dynamic Lagrangian with a kinetic
term `½ Ṡ²` and derives the Euler-Lagrange equation symbolically:

```
d/dt(∂L/∂Ṡ) − ∂L/∂S = 0
→ S̈ + (1+δ) / [t²·(S/Σ_V + 1)²·Σ_V] = 0
```

### Numerical layer (NumPy)

`simulate_field()` evaluates `modulated_entropy` over a time grid and counts
collapse events. It delegates to `medium-modulation` / `cosmic-moment` when
available, otherwise uses internal implementations.

## Optional stack delegation

Every external GenesisAeon package is guarded by a `try/except ImportError`:

```python
try:
    from medium_modulation.core import modulated_entropy as _ext_modulated_entropy
    _HAS_MODULATION = True
except ImportError:
    _HAS_MODULATION = False
```

This means the package installs and runs without the full stack — the
`[stack]` extra activates the integrations.
