from litestar import Litestar, MediaType, get


@get(path="/healthz", media_type=MediaType.TEXT)
async def health_check() -> str:
    return "healthy"


def create_server_app():
    app = Litestar(route_handlers=[health_check])
    return app
