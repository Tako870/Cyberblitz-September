# syntax=docker/dockerfile:1

FROM python:3.12-slim-bookworm

WORKDIR /CTF-Cyberblitz

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 9618

CMD [ "flask", "run", "--host=0.0.0.0", "--port=9618"]