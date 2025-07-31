from aiogram import Bot

from bot.services.notification.consumer import NotificateMessageConsumer
from nats.aio.client import Client
from nats.js.client import JetStreamContext


async def start_notificate_consumer(
    nc: Client, js: JetStreamContext, bot: Bot, subject: str, stream: str, durable: str
) -> None:
    consumer = NotificateMessageConsumer(
        nc=nc, js=js, bot=bot, subject=subject, stream=stream, durable=durable
    )
    await consumer.start()
