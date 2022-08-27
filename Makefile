start:
	docker-compose up --build -d
stop:
	docker-compose stop
logs:
	docker-compose logs -f
kill:
	docker-compose kill
clear:
	docker system prune --all --volumes
container:
	docker container ls -a
