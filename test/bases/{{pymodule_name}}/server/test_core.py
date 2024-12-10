import pytest

from litestar import Litestar
from litestar.status_codes import HTTP_200_OK
from litestar.testing import AsyncTestClient


@pytest.mark.anyio
async def test_health_check(test_client: AsyncTestClient["Litestar"]) -> None:
    response = await test_client.get("/healthz")
    assert response.status_code == HTTP_200_OK
    assert response.text == "healthy"
