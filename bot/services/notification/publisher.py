from nats.aio.errors import ErrConnectionClosed, ErrTimeout
from nats.js.client import JetStreamContext


async def notificate_message(
    js: JetStreamContext,
    message: str,
    chat_id: int,
    subject: str,
) -> bool:
    headers = {
        "Tg-Delayed-Chat-ID": str(chat_id),
    }
    try:
        await js.publish(
            subject=subject, payload=message.encode("utf-8"), headers=headers
        )
        return True
    except (TimeoutError, ErrConnectionClosed, ErrTimeout) as e:
        print(f"[NATS Error] Failed to publish message to chat_id={chat_id}: {e}")
        return False
    except Exception as e:
        print(f"[NATS Error] Unexpected exception during publish: {e}")
        return False
