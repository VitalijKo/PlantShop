FROM python:3.9

ENV PYTHONUNBUFFERED 1

ADD . /app
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000