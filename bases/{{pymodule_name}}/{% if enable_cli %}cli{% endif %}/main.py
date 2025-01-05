import click

from {{ pymodule_name }}.cli import subcommands


CONTEXT_SETTINGS = {
    "help_option_names": ["-h", "--help"],
}


@click.group(name="{{ cli_tool_name }}", context_settings=CONTEXT_SETTINGS)
def cli_entrypoint() -> None:
    """
    Command line interface for {{ project_name }}.
    """
    pass  # pragma: no cover


cli_entrypoint.add_command(subcommands.version.print_current_version)
cli_entrypoint.add_command(subcommands.server.cli_commands_server)
