FROM python:3.11-alpine
LABEL maintainer="adamdelezuch89@gmail.com"

ENV PYTHONUNBUFFERED 1

# Install system dependencies for psycopg2
RUN apk add --update --no-cache --virtual \
    .tmp-build-deps \
    build-base \
    postgresql-dev \
    musl-dev \
    zlib \
    zlib-dev \
    linux-headers 


COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

# Copy the project files into the container
COPY ./src /app/
WORKDIR /app

EXPOSE 8000

