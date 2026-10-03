import typer
from .db import init_db
from .services.pipeline import Pipeline

app = typer.Typer(no_args_is_help=True)

@app.command()
def ingest(path: str, exam: str = typer.Option(...), year: int | None = typer.Option(None), section: str | None = typer.Option(None)):
    init_db()
    result = Pipeline().ingest_pdf(path, exam, year, section)
    typer.echo(result)

if __name__ == "__main__":
    app()
