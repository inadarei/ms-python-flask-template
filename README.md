# ms-python-flask-template
A template project for a flask-based Python microservice

## Prerequisites:

1. Working Docker environment
2. GNU Make

## Supported Commands:

1. `make`  - build, start, and watch logs
2. `make start`
3. `make stop`
4. `make clean` - clean rebuild (for extreme debugging)
5. `make shell` - log into the running container of the microservice, for debugging
6. `make redis` - launch redis cli for debugging
7. `make logs` - tail combined logs from the service and the db
8. `make logs-app`
9. `make logs-db`
10. `make lint` - pylint code
11. `make test` - run unit and functional tests
12. `make add package="pytest"` - adds a module (in this case: "pytest") inside
a running container and saves it to the requirements.txt.
