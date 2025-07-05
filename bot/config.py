from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

CURRENT_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    BOT_TOKEN: str

    model_config = SettingsConfigDict(
        env_file=CURRENT_DIR / ".env", env_file_encoding="utf-8"
    )


settings = Settings()  # type: ignore
