FROM python:3-alpine

ENV PYTHONUNBUFFERED = 1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /code
COPY requirements.txt /code

RUN apk update && \
apk add --no-cache --virtual build-deps gcc python3-dev musl-dev && \
apk add postgresql-dev

RUN pip install -r requirements.txt

COPY . /code

EXPOSE 8000