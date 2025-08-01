import nats
from nats.aio.client import Client
from nats.aio.errors import ErrNoServers
from nats.js import JetStreamContext


async def connect_to_nats(servers: str | list[str]) -> tuple[Client, JetStreamContext]:
    try:
        nc: Client = await nats.connect(servers)  # type: ignore
        js: JetStreamContext = nc.jetstream()
        return nc, js
    except (TimeoutError, ErrNoServers, OSError) as e:
        print(f"[NATS Error] Failed to connect: {e}")
        raise
