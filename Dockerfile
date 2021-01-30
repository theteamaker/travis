FROM python:3-slim-buster

COPY *.py /app/
COPY requirements.txt /app/
COPY .env.dist /app/.env

RUN mkdir -p /app/commands
COPY commands/ /app/commands/

RUN mkdir /app/data

WORKDIR /app

RUN pip install -r requirements.txt && apt remove gcc -y && apt autoremove -y

CMD python main.py