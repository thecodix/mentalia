


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
	@docker exec -it mentalia-web-1 ./manage.py migrate


bash:
	@docker exec -it mentalia-web-1 bash

restart:
	-docker compose down
	-docker rmi mentalia-web
	docker compose build
	docker compose up -d
	make restore-data


isort:
	@docker exec -it mentalia-web-1 sh -c "isort ."

.PHONY: isort