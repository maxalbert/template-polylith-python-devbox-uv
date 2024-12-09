import click

from {{ pymodule_name }}.version import __version__


@click.command(name="version")
def print_current_version() -> None:
    """
    Print the current version.
    """
    click.echo(__version__)
