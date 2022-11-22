help:
	@echo "make test"

local:
	-docker-compose up

build:
	-docker-compose build