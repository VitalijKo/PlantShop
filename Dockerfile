FROM ubuntu:20.04

ADD . /app
WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update -y
RUN apt-get install python3.9 -y
RUN apt-get install python3-pip -y
RUN python3.9 -m pip install --upgrade setuptools
RUN apt-get install sudo ufw build-essential libpq-dev python3.9-dev libpython3.9-dev -y
RUN python3.9 -m pip install -r requirements.txt
RUN python3.9 -m pip install psycopg2-binary
RUN sudo ufw allow 8000

EXPOSE 8000