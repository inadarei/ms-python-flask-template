FROM python:3.8-alpine
MAINTAINER Irakli Nadareishvili

COPY . /app
WORKDIR /app

RUN apk upgrade --update \
 && apk add --no-cache build-base \
 && apk add bash \
 && pip install -r requirements.txt \
 && apk del build-base # reduce size \
 && echo never > /sys/kernel/mm/transparent_hugepage/enabled \
 && apk add make


CMD ["gunicorn", "-b 0.0.0.0", "--reload", \
     "-w 4", "service:app"]
