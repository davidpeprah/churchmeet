# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /churchmeet

RUN pip install Flask
RUN pip install mysql.connector

COPY . .

CMD ["python", "main.py"]

