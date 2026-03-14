# CLI Reference

## `ft simulate`

Run the unified field simulation.

```
Usage: ft simulate [OPTIONS]

Options:
  --steps INTEGER     Number of simulation time steps  [default: 100]
  --threshold FLOAT   Collapse detection threshold (0–1)  [default: 0.618]
  --s-a FLOAT         Initial area-entropy S_A  [default: 1.0]
  --s-v FLOAT         Initial volume-entropy S_V  [default: 1.618]
  --depth FLOAT       Modulation depth parameter  [default: 0.5]
```

**Examples**

```bash
ft simulate
ft simulate --steps 500 --threshold 0.5
ft simulate --s-a 2.0 --s-v 3.14 --depth 0.3
```

---

## `ft lagrangian`

Derive and display the symbolic Lagrangian and Euler-Lagrange equation.

```bash
ft lagrangian
```

Output example:

```
Lagrangian L       = S_A*S_V/(S_A + S_V) - (delta + 1)/t**2
Euler-Lagrange     = Eq(S(t).diff(t, t) + (delta + 1)/(t**2*(S(t)/Sigma_V + 1)**2*Sigma_V), 0)
```

---

## `ft version`

Print the installed version.

```bash
ft version
```
