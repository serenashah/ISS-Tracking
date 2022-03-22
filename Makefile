NAME ?= serenashah

all: build run push

images:
	docker images | grep ${NAME}

ps:
	docker ps -a | grep ${NAME}

build:
	docker build -t ${NAME}/flask-iss-app:latest .

run:
	docker run --name "serenashah-iss-app" -d -p 5028:5000 --rm -v \${PWD}:/iss_app ${NAME}/flask-iss-app:latest

push:
	docker push ${NAME}/flask-iss-app:latest
