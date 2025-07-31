from pathlib import Path
from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict

from nats.js.api import RetentionPolicy, StorageType

CURRENT_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_IDS: list[int]
    REDIS_URL: str
    MONGO_URI: str
    NATS_SERVERS: str
    NATS_SUBJECT: str = "notifications.broadcast"
    NATS_STREAM: str = "BroadcastStream"
    NATS_NOTIFICATE_DURABLE_NAME: str = "notificator"

    model_config = SettingsConfigDict(
        env_file=CURRENT_DIR / ".env", env_file_encoding="utf-8"
    )

    @property
    def NATS_STREAM_CONFIG(self) -> dict[str, Any]:
        return {
            "name": self.NATS_STREAM,
            "subjects": [self.NATS_SUBJECT],
            "retention": RetentionPolicy.LIMITS,
            "max_bytes": 300 * 1024 * 1024,
            "max_msg_size": 10 * 1024 * 1024,
            "storage": StorageType.FILE,
            "allow_direct": True,
        }


settings = Settings()  # type: ignore
