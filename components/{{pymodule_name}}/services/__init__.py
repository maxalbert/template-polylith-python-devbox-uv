from litestar import Litestar
import svcs


def get_registry(app: Litestar) -> svcs.Registry:
    return app.state.registry
