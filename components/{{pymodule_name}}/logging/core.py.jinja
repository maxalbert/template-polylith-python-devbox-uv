import structlog

from {{ pymodule_name }}.settings import settings


def configure_structlog(use_colors: bool | None = None):
    if use_colors is None:
        use_colors = settings.logging.use_colors

    cr = structlog.dev.ConsoleRenderer(colors=use_colors)
    structlog.configure(processors=structlog.get_config()["processors"][:-1] + [cr])


configure_structlog()
structlog_logger = structlog.get_logger()
