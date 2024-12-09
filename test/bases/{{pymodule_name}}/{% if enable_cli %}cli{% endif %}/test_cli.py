import textwrap

from click.testing import CliRunner

from {{ pymodule_name }}.cli import cli_entrypoint
from {{ pymodule_name }}.version import __version__


def test_cli_without_arguments() -> None:
    runner = CliRunner()
    result = runner.invoke(cli_entrypoint)

    expected_output = textwrap.dedent(
        """\
        Usage: {{ cli_tool_name }} [OPTIONS] COMMAND [ARGS]...

          Command line interface for {{ project_name }}.

        Options:
          -h, --help  Show this message and exit.

        Commands:
          version  Print the current version.
        """
    )

    assert result.output == expected_output


def test_version() -> None:
    runner = CliRunner()
    result = runner.invoke(cli_entrypoint, "version")

    assert result.output.strip() == __version__
