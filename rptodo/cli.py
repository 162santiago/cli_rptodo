from typing import Optional
from rptodo import __app_name__ , __version__

import typer

app = typer.Typer()

def version_callback(value:bool) ->None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()
    

@app.callback()
def main(
    version : Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback= version_callback,
        is_eager=True,
    )
)->None:
    return