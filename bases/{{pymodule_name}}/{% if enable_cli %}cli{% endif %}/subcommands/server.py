import click

from {{ pymodule_name }}.api import run_api_server


@click.group(name="server")
def cli_commands_server() -> None:
    """
    Commands to run and manage the server.
    """
    pass


@cli_commands_server.command(name="run")
@click.option(
    "-h",
    "--host",
    "host",
    type=click.STRING,
    default="localhost",
    help="Server host (default: localhost)",
)
@click.option(
    "-p",
    "--port",
    "port",
    type=click.INT,
    default=8000,
    help="Server port (default: 8000)",
)
def run_server(host: str, port: int):
    """
    Start the server process.
    """
    run_api_server(host=host, port=port)
