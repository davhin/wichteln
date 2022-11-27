FROM python:3.10-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y gcc libffi-dev g++
WORKDIR /app


ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.14
RUN pip install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION"
ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev --no-root

COPY . /app

CMD ["poetry", "run", "streamlit", "run", "/app/app.py"]