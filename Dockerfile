FROM python:3.10

WORKDIR /home/flask-project

ENV PYTHONBUFFERED 1


COPY ./requirements.txt .
COPY ./migrations ./migrations
COPY ./logs ./logs

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
