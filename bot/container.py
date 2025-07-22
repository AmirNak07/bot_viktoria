from typing import Any

from bot.database.collections import MongoCollections
from bot.database.mongodb import MongoDB
from bot.repositories.event_repo import EventsRepository
from bot.repositories.user_repo import UsersRepository
from bot.services.event_service import EventsService
from bot.services.user_service import UsersService


def build_container(connection_uri: str, db_name: str) -> dict[str, Any]:
    mongo = MongoDB(connection_uri, db_name)
    collections = MongoCollections(mongo)

    user_repo = UsersRepository(collections.users)
    event_repo = EventsRepository(collections.events)

    user_service = UsersService(user_repo)
    event_service = EventsService(event_repo)

    return {
        "mongo": mongo,
        "collections": collections,
        "user_repo": user_repo,
        "event_repo": event_repo,
        "user_service": user_service,
        "event_service": event_service,
    }
