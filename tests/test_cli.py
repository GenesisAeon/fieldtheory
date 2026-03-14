"""Tests for the fieldtheory CLI."""

from typer.testing import CliRunner

from fieldtheory import __version__
from fieldtheory.cli import app

runner = CliRunner()


def test_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert __version__ in result.output


def test_simulate_default():
    result = runner.invoke(app, ["simulate"])
    assert result.exit_code == 0
    out = result.output.lower()
    assert "s_mod" in out or "mean" in out or "simulation" in out


def test_simulate_custom_steps():
    result = runner.invoke(app, ["simulate", "--steps", "50"])
    assert result.exit_code == 0


def test_simulate_shows_cosmic_moments():
    result = runner.invoke(app, ["simulate", "--steps", "20"])
    assert result.exit_code == 0
    assert "cosmic" in result.output.lower() or "moment" in result.output.lower()


def test_lagrangian_command():
    result = runner.invoke(app, ["lagrangian"])
    assert result.exit_code == 0
    # Should contain some symbolic output
    assert "=" in result.output or "Eq" in result.output or "Lagrangian" in result.output


def test_simulate_all_options():
    result = runner.invoke(
        app,
        [
            "simulate",
            "--steps",
            "30",
            "--threshold",
            "0.5",
            "--s-a",
            "2.0",
            "--s-v",
            "3.0",
            "--depth",
            "0.3",
        ],
    )
    assert result.exit_code == 0
