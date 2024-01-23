


makemigrations:
	@docker exec -it mentalia-web-1 ./manage.py makemigrations examenes

migrate:
	docker exec -it mentalia-web-1 ./manage.py migrate

superuser:
	@docker exec -it mentalia-web-1 ./manage.py createsuperuser

empty-migration:
	python manage.py makemigrations examenes --empty

dump-data:
	docker exec -it mentalia-web-1 ./manage.py dumpdata examenes > datos_examenes.json


restore-data:
	@docker exec mentalia-web-1 ./manage.py migrate --no-input


bash:
	@docker exec -it mentalia-web-1 bash

restart:
	-docker compose down
	-docker rmi mentalia-web
	docker compose build
	docker compose up -d
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