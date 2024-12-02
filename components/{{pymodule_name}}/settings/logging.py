from pydantic import BaseModel


class LoggingSettings(BaseModel):
    level: str = "DEBUG"
    use_colors: bool = True
