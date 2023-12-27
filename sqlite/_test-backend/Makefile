#* Variables
SHELL := /usr/bin/env bash

#* Setup
.PHONY: $(shell sed -n -e '/^$$/ { n ; /^[^ .\#][^ ]*:/ { s/:.*$$// ; p ; } ; }' $(MAKEFILE_LIST))
.DEFAULT_GOAL := help

help: ## list make commands
	@echo ${MAKEFILE_LIST}
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

#* Docker Compose
build: ## dc build
	docker-compose build

up: ## dc up --build --remove-orphans
	docker-compose up --build --remove-orphans

up-prod: ## dc up -d
	docker-compose up -d

down: ## dc down
	docker-compose down

logs: ## dc logs
	docker-compose logs -f

open: ## open localhost
	open http://0.0.0.0/

open-api: ## open api swagger page
	open http://0.0.0.0/api/docs

#* Cleaning
pycache-remove: ## cleanup subcommand - pycache-remove
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

dsstore-remove: ## cleanup subcommand - dsstore-remove
	find . | grep -E ".DS_Store" | xargs rm -rf

mypycache-remove: ## cleanup subcommand - mypycache-remove
	find . | grep -E ".mypy_cache" | xargs rm -rf

ipynbcheckpoints-remove: ## cleanup subcommand - ipynbcheckpoints-remove
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf

pytestcache-remove: ## cleanup subcommand - pytestcache-remove
	find . | grep -E ".pytest_cache" | xargs rm -rf

build-remove: ## build-remove
	rm -rf build/

cleanup: pycache-remove dsstore-remove mypycache-remove ipynbcheckpoints-remove pytestcache-remove
