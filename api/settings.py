from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8000)
    reload: bool = Field(default=False)
    log_level: str = Field(default="info")

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
