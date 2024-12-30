import svcs

# from pyqcrbox.services import get_registry, init_app_registry
from pyqcrbox.services import get_registry


def test_init_app_registry(server_app):
    registry = get_registry(server_app)
    # server_app = init_app_registry(server_app)
    assert isinstance(registry, svcs.Registry)
