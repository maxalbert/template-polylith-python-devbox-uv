from pydantic_settings import BaseSettings, SettingsConfigDict


class SettingsBaseModel(BaseSettings):
    model_config = SettingsConfigDict(
        validate_assignment=True,
    )
