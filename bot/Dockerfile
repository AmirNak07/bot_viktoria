FROM python:3.12-alpine

RUN pip install --upgrade --no-cache-dir uv==0.7.19

WORKDIR /app

COPY pyproject.toml uv.lock* ./
RUN uv sync --locked --no-dev --group bot

COPY bot ./bot

CMD [ "uv", "run", "-m", "--no-dev", "bot.main" ]
