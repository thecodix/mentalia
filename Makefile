


makemigrations:
	@docker exec -it puntoycoma-web-1 ./manage.py makemigrations examenes

migrate:
	docker exec -it puntoycoma-web-1 ./manage.py migrate

superuser:
	@docker exec -it puntoycoma-web-1 ./manage.py createsuperuser

empty-migration:
	python manage.py makemigrations examenes --empty

dump-data:
	docker exec -it puntoycoma-web-1 ./manage.py dumpdata examenes > datos_examenes.json


restore-data:
	@docker exec -it puntoycoma-web-1 ./manage.py migrate


bash:
	@docker exec -it puntoycoma-web-1 bash

restart:
	-docker compose down
	-docker rmi puntoycoma-web
	docker compose build
	docker compose up -d
	make restore-data


isort:
	@docker exec -it puntoycoma-web-1 sh -c "isort ."

.PHONY: isort