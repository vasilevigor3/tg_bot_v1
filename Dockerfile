FROM python:latest

ADD yahoo/yahoo.py /
COPY . .
RUN pip install -r requirements.txt