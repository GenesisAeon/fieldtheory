"""fieldtheory CLI – unified Lagrangian simulation and symbolic derivation."""

from __future__ import annotations

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from . import __version__
from .core import derive_lagrangian, simulate_field

app = typer.Typer(
    name="ft",
    help="fieldtheory – unified S\u221dA/S\u221dV Lagrangian field simulation.",
    add_completion=True,
    rich_markup_mode="rich",
)
console = Console()


@app.command()
def simulate(
    steps: int = typer.Option(100, help="Number of simulation time steps"),
    threshold: float = typer.Option(0.618, help="Collapse detection threshold (0\u20131)"),
    s_a: float = typer.Option(1.0, help="Initial area-entropy S_A"),
    s_v: float = typer.Option(1.618, help="Initial volume-entropy S_V"),
    depth: float = typer.Option(0.5, help="Modulation depth parameter"),
) -> None:
    """[bold]Run the unified field simulation[/bold] (modulation + collapse detection)."""
    result = simulate_field(steps=steps, threshold=threshold, s_a0=s_a, s_v0=s_v, depth_val=depth)

    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_row("[dim]steps[/dim]", str(steps))
    table.add_row("[dim]threshold[/dim]", f"{threshold:.3f}")
    table.add_row("[bold green]mean S_mod[/bold green]", f"{result['S_mod_mean']:.6f}")
    table.add_row("[bold magenta]cosmic moments[/bold magenta]", str(result["cosmic_moments"]))

    console.print(Panel(table, title="[bold cyan]fieldtheory simulation[/bold cyan]", expand=False))


@app.command()
def lagrangian() -> None:
    """[bold]Derive and display[/bold] the symbolic Euler-Lagrange equation."""
    result = derive_lagrangian()
    console.print(f"[bold cyan]Lagrangian L[/bold cyan]       = {result['lagrangian']}")
    console.print(f"[bold cyan]Euler-Lagrange[/bold cyan]     = {result['euler_lagrange']}")


@app.command()
def version() -> None:
    """Show the fieldtheory version."""
    console.print(f"fieldtheory [bold]{__version__}[/bold]")


if __name__ == "__main__":
    app()
