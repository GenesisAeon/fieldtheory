"""Tests for fieldtheory.core – simulation, Lagrangian, modulation."""

import pytest
import sympy as sp

from fieldtheory.core import (
    _modulated_entropy_internal,
    derive_lagrangian,
    modulated_entropy,
    simulate_field,
)

# ---------------------------------------------------------------------------
# modulated_entropy
# ---------------------------------------------------------------------------


def test_modulated_entropy_positive():
    val = modulated_entropy(1.0, 1.618, 0.5)
    assert val > 0


def test_modulated_entropy_t_zero_limit():
    """At large t, modulation vanishes and result approaches harmonic mean."""
    s_a, s_v, d = 2.0, 3.0, 1.0
    harmonic = (s_a * s_v) / (s_a + s_v)
    val_large_t = modulated_entropy(s_a, s_v, d, amplitude=1.0, t_val=1000.0)
    assert abs(val_large_t - harmonic) < 1e-3


def test_modulated_entropy_internal_matches_public():
    """Public and internal implementations agree (no external package installed)."""
    args = (1.0, 1.618, 0.5, 1.0, 2.0)
    assert modulated_entropy(*args) == pytest.approx(_modulated_entropy_internal(*args))


def test_modulated_entropy_internal_depth_zero():
    """Depth 0 → modulation amplitude is unchanged, formula still runs cleanly."""
    val = _modulated_entropy_internal(1.0, 2.0, 0.0, amplitude=0.0)
    harmonic = (1.0 * 2.0) / (1.0 + 2.0)
    assert val == pytest.approx(harmonic)


# ---------------------------------------------------------------------------
# derive_lagrangian
# ---------------------------------------------------------------------------


def test_derive_lagrangian_returns_dict():
    result = derive_lagrangian()
    assert "lagrangian" in result
    assert "euler_lagrange" in result


def test_derive_lagrangian_is_sympy():
    result = derive_lagrangian()
    assert isinstance(result["lagrangian"], sp.Basic)
    assert isinstance(result["euler_lagrange"], sp.Eq)


def test_lagrangian_has_expected_symbols():
    from fieldtheory.core import S_A, S_V, delta, t

    L = derive_lagrangian()["lagrangian"]
    free = L.free_symbols
    assert S_A in free
    assert S_V in free
    assert delta in free
    assert t in free


def test_euler_lagrange_is_equation():
    eq = derive_lagrangian()["euler_lagrange"]
    assert isinstance(eq, sp.Eq)


# ---------------------------------------------------------------------------
# simulate_field
# ---------------------------------------------------------------------------


def test_simulate_returns_expected_keys():
    result = simulate_field(steps=20)
    assert "S_mod_mean" in result
    assert "S_mod_series" in result
    assert "cosmic_moments" in result


def test_simulate_S_mod_mean_positive():
    result = simulate_field(steps=50)
    assert result["S_mod_mean"] > 0


def test_simulate_series_shape():
    result = simulate_field(steps=37)
    assert len(result["S_mod_series"]) == 37


def test_simulate_cosmic_moments_non_negative():
    result = simulate_field(steps=50, threshold=0.618)
    assert result["cosmic_moments"] >= 0


def test_simulate_high_threshold_gives_more_moments():
    """Higher threshold → more samples below it → more detected moments."""
    low = simulate_field(steps=100, threshold=0.1)["cosmic_moments"]
    high = simulate_field(steps=100, threshold=0.99)["cosmic_moments"]
    assert high >= low


def test_simulate_custom_field_params():
    result = simulate_field(steps=30, s_a0=2.0, s_v0=3.0, depth_val=0.1)
    assert result["S_mod_mean"] > 0


def test_simulate_golden_ratio_defaults():
    """Default params use S_V = φ ≈ 1.618 (golden ratio) — just verify it runs."""
    result = simulate_field()
    assert isinstance(result["S_mod_mean"], float)
