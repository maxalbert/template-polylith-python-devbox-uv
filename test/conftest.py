import pytest

from pyqcrbox.logging import configure_structlog


@pytest.fixture(scope="session", autouse=True)
def disable_colored_logging_output():
    configure_structlog(use_colors=False)
