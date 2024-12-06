from pydantic_settings import SettingsConfigDict

from {{ pymodule_name }}.settings.base import SettingsBaseModel
from {{ pymodule_name }}.settings.logging import LoggingSettings


class Settings(SettingsBaseModel):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=[".env.local"],
        env_nested_delimiter="__",
        env_prefix="{{ env_vars_prefix }}__",
    )

    logging: LoggingSettings = LoggingSettings()


settings = Settings()
