default: start logs

service:=ms-template-microservice

.PHONY: start
start:
	docker-compose up -d

.PHONY: stop
stop:
	docker-compose down

.PHONY: restart
restart: stop start

.PHONY: ps
ps:
	docker-compose ps

.PHONY: logs
logs:
	docker-compose logs -f

.PHONY: logs-db
logs-db:
	docker-compose logs -f ms-redis

.PHONY: logs-app
logs-app:
	docker-compose logs -f ${service}

# connect to redis cli for debugging
.PHONY: redis
redis:
	docker exec -it ms-redis redis-cli -a 4n_ins3cure_P4ss

# connect to the microservice cli for debugging
.PHONY: shell
shell:
	docker-compose exec ${service} bash

.PHONY: build
build:
	docker-compose build --no-cache

.PHONY: clean
clean: stop build start

.PHONY: install-package-in-container
install-package-in-container:
	docker-compose exec ${service} pip install ${package}
	docker-compose exec ${service} pip freeze > requirements.txt

.PHONY: add
add: start install-package-in-container build

.PHONY: deps
deps:
	docker-compose exec ${service} pip install -r requirements.txt

.PHONY: lint
lint:
	docker-compose exec ${service} pylint service.py src/*.py tests/**/*.py

.PHONY: test
test: start test-run-only

.PHONY: test-run-only
test-run-only:
	docker-compose exec ${service} pytest
