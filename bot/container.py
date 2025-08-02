from typing import Any

from bot.config import settings
from bot.database.collections import MongoCollections
from bot.database.mongodb import MongoDB
from bot.repositories.event_repo import EventsRepository
from bot.repositories.user_repo import UsersRepository
from bot.services.event_service import EventsService
from bot.services.user_service import UsersService
from bot.utils.nats_connect import connect_to_nats
from nats.js.api import StreamConfig


async def build_container(connection_uri: str, db_name: str) -> dict[str, Any]:
    mongo = MongoDB(connection_uri, db_name)

    try:
        await mongo._client.server_info()  # Force connection test
    except Exception as e:
        print("[MongoDB Error] Failed to connect:", e)
        raise

    collections = MongoCollections(mongo)

    user_repo = UsersRepository(collections.users)
    event_repo = EventsRepository(collections.events)

    user_service = UsersService(user_repo)
    event_service = EventsService(event_repo)

    nc, js = await connect_to_nats(servers=settings.NATS_SERVERS)
    stream_config = StreamConfig(**settings.NATS_STREAM_CONFIG)
    await js.add_stream(stream_config)

    return {
        "mongo": mongo,
        "collections": collections,
        "user_repo": user_repo,
        "event_repo": event_repo,
        "user_service": user_service,
        "event_service": event_service,
        "nc": nc,
        "js": js,
    }
