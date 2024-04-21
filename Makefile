greq:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

up:
	docker compose up --build -d

down:
	docker compose down

ps:
	docker compose ps

psa:
	docker compose ps -a

activate:
	poetry shell
	