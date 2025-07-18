FROM python:3.12-alpine

RUN pip install --upgrade --no-cache-dir uv==0.7.19

WORKDIR /app

COPY pyproject.toml uv.lock* ./
RUN uv sync --no-dev --locked --group parser

COPY scheduler ./scheduler

CMD [ "uv", "run", "-m", "--no-dev", "scheduler.main" ]
