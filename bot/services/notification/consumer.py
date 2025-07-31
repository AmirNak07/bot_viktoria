from contextlib import suppress

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest

from nats.aio.client import Client
from nats.aio.msg import Msg
from nats.js import JetStreamContext


class NotificateMessageConsumer:
    def __init__(
        self,
        nc: Client,
        js: JetStreamContext,
        bot: Bot,
        subject: str,
        stream: str,
        durable: str,
    ) -> None:
        self.nc = nc
        self.js = js
        self.bot = bot
        self.subject = subject
        self.stream = stream
        self.durable = durable

    async def start(self) -> None:
        self.stream_sub = await self.js.subscribe(
            subject=self.subject,
            stream=self.stream,
            cb=self.on_message,
            manual_ack=True,
            durable=self.durable,
        )

    async def on_message(self, msg: Msg) -> None:
        chat_id = msg.headers.get("Tg-Delayed-Chat-ID")  # type: ignore
        message = msg.data.decode("utf-8")
        with suppress(TelegramBadRequest):
            await self.bot.send_message(chat_id=chat_id, text=message)  # type: ignore
        await msg.ack()

    async def unsubscribe(self) -> None:
        if self.stream_sub:
            await self.stream_sub.unsubscribe()
