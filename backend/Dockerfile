FROM python:3.12-bullseye

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app/

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# COPY ./pyproject.toml ./poetry.lock* /app/
RUN poetry install
RUN chmod +x /app/run.sh

ENV PYTHONPATH=/

EXPOSE 8001

CMD ["./run.sh"]
