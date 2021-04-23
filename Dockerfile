FROM python:3.6-slim

ENV PYTHONUNBUFFERED=1

#RUN mkdir /app

WORKDIR /app

#COPY . /app
COPY . .

RUN pip install -r requirements.txt

# Do ot use it with docker-compose running
CMD python manage.py runserver 0.0.0.0:8000

