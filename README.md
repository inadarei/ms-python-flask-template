# ms-python-flask-template
A template project for a flask-based Python microservice

## Prerequisites:

1. Working Docker environment
2. GNU Make

## Commands:

1. make  - build, start, and watch logs
2. make start
3. make stop
4. make clean - clean rebuild (for extreme debugging)
5. make shell - log into the running container of the microservice, for debugging
6. make redis - launch redis cli for debugging
7. make logs - tail combined logs from the service and the db
8. make logs-app
9. make logs-db 