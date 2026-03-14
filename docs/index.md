# fieldtheory

**The unifying field theory of the GenesisAeon stack.**

Derives the full Lagrangian from S∝A/S∝V duality, applies medium-modulation, detects cosmic-moment collapse and exports to entropy-table.

## Quickstart

```bash
pip install fieldtheory
ft simulate --steps 100
ft lagrangian
```

## The Lagrangian

```
L = S_A·S_V / (S_A + S_V)  −  (1 + δ) / t²
```

| Term | Role |
|------|------|
| `S_A·S_V / (S_A + S_V)` | Harmonic duality balance (S∝A ↔ S∝V) |
| `(1 + δ) / t²` | Depth-weighted collapse potential |

## Stack Integration

| Package | Role | Required |
|---------|------|----------|
| `medium-modulation` | Modulated entropy computation | Optional |
| `cosmic-moment` | Collapse event detection | Optional |
| `entropy-governance` | Duality factor | Optional |
| `entropy-table` | Result export | Optional |

All integrations degrade gracefully — the core simulation runs standalone.

## Commands

| Command | Description |
|---------|-------------|
| `ft simulate` | Run the unified field simulation |
| `ft lagrangian` | Display the symbolic Euler-Lagrange equation |
| `ft version` | Show version |
