import uvicorn

from litestar import Litestar, MediaType, get


@get(path="/healthz", media_type=MediaType.TEXT)
async def health_check() -> str:
    return "healthy"


app = Litestar(route_handlers=[health_check])


def run_api_server(host: str = "localhost", port: int = 8000):
    uvicorn_log_level = "info"
    uvicorn.run(app, host=host, port=port, log_level=uvicorn_log_level)
