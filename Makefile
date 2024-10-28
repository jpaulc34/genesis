# Makefile
.PHONY: install run test

install:
	poetry install

run:
	poetry run uvicorn app.main:app --reload

build:
	docker-compose build

up:
	docker-compose up -d

build-up: build up

down:
	docker-compose down

test:
	poetry run pytest