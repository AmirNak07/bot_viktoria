FROM python:3.12-alpine

RUN pip install --upgrade --no-cache-dir uv==0.7.19

WORKDIR /app

COPY pyproject.toml uv.lock* ./
RUN uv pip compile --group bot --output-file requirements.txt && pip install -r --no-cache-dir requirements.txt

COPY bot ./bot

CMD [ "python", "bot/main.py" ]
