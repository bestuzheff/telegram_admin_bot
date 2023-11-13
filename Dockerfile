FROM python:3.10-slim

RUN apt-get update
RUN apt-get --force-yes -y install libzbar0

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY admin_bot.py admin_bot.py
COPY .env .env

CMD [ "python3", "admin_bot.py"]