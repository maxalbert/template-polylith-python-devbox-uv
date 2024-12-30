from typing import TYPE_CHECKING
from collections.abc import AsyncIterator

import pytest

from litestar import Litestar
from litestar.testing import AsyncTestClient

from {{ pymodule_name }}.logging import configure_structlog
from {{ pymodule_name }}.server import app

if TYPE_CHECKING:
    from litestar import Litestar


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture(scope="session", autouse=True)
def disable_colored_logging_output() -> None:
    configure_structlog(use_colors=False)


@pytest.fixture(scope="function")
async def test_client() -> AsyncIterator[AsyncTestClient["Litestar"]]:
    async with AsyncTestClient(app=app) as client:
        yield client
