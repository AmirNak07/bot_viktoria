from nats.js.client import JetStreamContext


async def notificate_message(
    js: JetStreamContext,
    message: str,
    chat_id: int,
    subject: str,
) -> None:
    headers = {
        "Tg-Delayed-Chat-ID": str(chat_id),
    }
    await js.publish(subject=subject, payload=message.encode("utf-8"), headers=headers)
