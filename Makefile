
up:
	docker compose up -d

makemigrations:
	@docker exec -it mentalia-web-1 ./manage.py makemigrations examenes

migrate:
	docker exec -it mentalia-web-1 ./manage.py migrate

superuser:
	@docker exec -it mentalia-web-1 ./manage.py createsuperuser

empty-migration:
	python manage.py makemigrations examenes --empty

dump-data:
	docker exec -it mentalia-web-1 ./manage.py dumpdata examenes > data/datos_24_07_02.json 2> data/warnings_24_07_02.log


restore-data:
	@docker exec mentalia-web-1 ./manage.py migrate --no-input


bash:
	@docker exec -it mentalia-web-1 bash

restart:
	-docker compose down
	-docker rmi mentalia-web
	docker compose build
	make up
	sleep 2  # Give the container some time to start up properly
	make restore-data

restartgpt:
	-docker-compose down --volumes
	docker-compose build
	docker-compose up -d
	sleep 5  # Give the container some time to start up properly
	docker-compose exec web ./manage.py migrate

isort:
	@docker exec -it mentalia-web-1 sh -c "isort ."

.PHONY: isort

pylint:
	@docker exec -it mentalia-web-1 sh -c "pylint . --recursive=true"

bandit:
	@docker exec -it mentalia-web-1 sh -c "bandit -c pyproject.toml -r ."

linters: isort pylint bandit

test:
	@docker exec -it mentalia-web-1 sh -c "pytest"

static:
	@docker exec -it mentalia-web-1 ./manage.py collectstatic