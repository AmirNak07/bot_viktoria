from aiogram import Bot
from aiogram.exceptions import TelegramAPIError

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
        try:
            self.stream_sub = await self.js.subscribe(
                subject=self.subject,
                stream=self.stream,
                cb=self.on_message,
                manual_ack=True,
                durable=self.durable,
            )
        except Exception as e:
            print(f"[NATS Error] Failed to subscribe to {self.subject}: {e}")
            raise

    async def on_message(self, msg: Msg) -> None:
        chat_id = msg.headers.get("Tg-Delayed-Chat-ID")  # type: ignore
        message = msg.data.decode("utf-8")

        try:
            await self.bot.send_message(chat_id=chat_id, text=message)  # type: ignore
        except TelegramAPIError as e:
            print(f"[Telegram Error] Failed to send message to {chat_id}: {e}")
        except Exception as e:
            print(f"[Unknown Error] in on_message for chat_id={chat_id}: {e}")

        await msg.ack()

    async def unsubscribe(self) -> None:
        if self.stream_sub:
            await self.stream_sub.unsubscribe()
