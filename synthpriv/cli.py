# synthpriv/cli.py
import typer  # CLI framework
from synthpriv.trainer import train_copula  # Synthetic data trainer
from synthpriv.eval import evaluate  # Utility evaluator
from synthpriv.catalog import catalog_add, catalog_list  # Data catalog

app = typer.Typer()

# CLI command: Train synthetic data model
@app.command()
def train(csv_path: str, epsilon: float, delta: float = 1e-5, epochs: int = 100, seed: int = 42):
    """Train GaussianCopula and save synthetic data."""
    synth_path, col_eps = train_copula(csv_path, epsilon, delta, epochs, seed)
    typer.echo(f"Synthetic data saved to {synth_path}\nColumn epsilons: {col_eps}")

# CLI command: Evaluate synthetic data utility/privacy
@app.command()
def evaluate_cmd(real_csv: str, synth_csv: str):
    """Evaluate synthetic data utility/privacy."""
    metrics, report_dir = evaluate(real_csv, synth_csv)
    typer.echo(f"Metrics: {metrics}\nReport: {report_dir}")

# CLI command: Catalog management (add/list)
@app.command()
def catalog(cmd: str = typer.Argument(..., help='add|list'), path: str = None):
    if cmd == 'add' and path:
        catalog_add(path)
    elif cmd == 'list':
        typer.echo(catalog_list())
    else:
        typer.echo('Invalid catalog command')

if __name__ == "__main__":
    app()
