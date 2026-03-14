"""Unified Lagrangian field theory: S∝A/S∝V duality, medium modulation, cosmic-moment collapse."""

from __future__ import annotations

import numpy as np
import sympy as sp

# ---------------------------------------------------------------------------
# Optional GenesisAeon stack integrations
# ---------------------------------------------------------------------------

try:
    from medium_modulation.core import (
        modulated_entropy as _ext_modulated_entropy,  # type: ignore[import-not-found]
    )

    _HAS_MODULATION = True
except ImportError:
    _HAS_MODULATION = False

try:
    from cosmic_moment.core import CosmicMoment  # type: ignore[import-not-found]

    _HAS_COSMIC = True
except ImportError:
    _HAS_COSMIC = False

try:
    import entropy_governance  # type: ignore[import-not-found]  # noqa: F401

    _HAS_GOVERNANCE = True
except ImportError:
    _HAS_GOVERNANCE = False

# ---------------------------------------------------------------------------
# Symbolic field setup
# ---------------------------------------------------------------------------

t = sp.Symbol("t", real=True, positive=True)
S_A, S_V, delta = sp.symbols("S_A S_V delta", positive=True)

# Unified symbolic Lagrangian
# T = harmonic mean of S_A and S_V  — encodes the S∝A/S∝V duality balance
# V = depth-weighted collapse potential  — drives cosmic-moment singularity
L = (S_A * S_V) / (S_A + S_V) - (1 + delta) / t**2

# ---------------------------------------------------------------------------
# Internal modulated entropy (fallback when medium-modulation is not installed)
# ---------------------------------------------------------------------------


def _modulated_entropy_internal(
    s_a: float,
    s_v: float,
    d: float,
    amplitude: float = 1.0,
    t_val: float = 1.0,
) -> float:
    """S∝A/S∝V harmonic duality with exponential depth modulation."""
    harmonic = (s_a * s_v) / (s_a + s_v)
    phi = amplitude * np.exp(-d * t_val)
    return float(harmonic * (1.0 + phi))


def modulated_entropy(
    s_a: float,
    s_v: float,
    d: float,
    amplitude: float = 1.0,
    t_val: float = 1.0,
) -> float:
    """Modulated entropy; delegates to medium-modulation if installed, otherwise internal."""
    if _HAS_MODULATION:
        return float(_ext_modulated_entropy(s_a, s_v, d, amplitude, t_val))  # type: ignore[arg-type]
    return _modulated_entropy_internal(s_a, s_v, d, amplitude, t_val)


# ---------------------------------------------------------------------------
# Euler-Lagrange derivation
# ---------------------------------------------------------------------------


def derive_lagrangian() -> dict[str, sp.Basic]:
    """
    Derive the Euler-Lagrange equation for the unified field Lagrangian.

    Treats S(t) as the primary dynamical field with a kinetic term ½ Ṡ².
    The collapse potential couples the field to the S∝V reference scale.

    Returns a dict with keys:
      - ``lagrangian``:     symbolic L (static, no kinetic term, for inspection)
      - ``euler_lagrange``: EL equation as a SymPy Eq
    """
    S_func = sp.Function("S")(t)

    # Dynamic Lagrangian: kinetic term + depth-weighted collapse potential
    L_dyn = sp.Rational(1, 2) * S_func.diff(t) ** 2 - (1 + delta) / (t**2 * (S_func / S_V + 1))

    dL_dqdot = sp.diff(L_dyn, S_func.diff(t))
    dL_dq = sp.diff(L_dyn, S_func)
    el_eq = sp.Eq(sp.diff(dL_dqdot, t) - dL_dq, 0)

    return {"lagrangian": L, "euler_lagrange": el_eq}


# ---------------------------------------------------------------------------
# Numerical simulation
# ---------------------------------------------------------------------------


def simulate_field(
    steps: int = 100,
    threshold: float = 0.618,
    s_a0: float = 1.0,
    s_v0: float = 1.618,
    depth_val: float = 0.5,
) -> dict:
    """
    Run the unified field simulation.

    Computes the modulated entropy series over time, then detects cosmic-moment
    collapse events (threshold crossings of the normalised field amplitude).

    Args:
        steps:      Number of time steps.
        threshold:  Fractional amplitude threshold for collapse detection (0–1).
        s_a0:       Initial area-entropy value.
        s_v0:       Initial volume-entropy value.
        depth_val:  Modulation depth parameter.

    Returns:
        dict with ``S_mod_mean`` (float), ``S_mod_series`` (ndarray),
        ``cosmic_moments`` (int).
    """
    t_vals = np.linspace(0.1, 10.0, steps)
    S_mod = np.array([modulated_entropy(s_a0, s_v0, depth_val, 1.0, ti) for ti in t_vals])

    if _HAS_COSMIC:
        cm = CosmicMoment()  # type: ignore[misc]
        moments = len(cm.detect(threshold=threshold))
    else:
        # Internal collapse detection: count samples below fractional threshold
        cutoff = threshold * float(S_mod.max())
        moments = int(np.sum(S_mod < cutoff))

    return {
        "S_mod_mean": float(np.mean(S_mod)),
        "S_mod_series": S_mod,
        "cosmic_moments": moments,
    }
