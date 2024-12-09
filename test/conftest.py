import pytest

from {{ pymodule_name }}.logging import configure_structlog


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="session", autouse=True)
def disable_colored_logging_output() -> None:
    configure_structlog(use_colors=False)
