.PHONY: all
SIM_DIRS := $(shell find app -type d -name "sim")

all: up sim

restart: down up term

up:
	sudo docker-compose up -d
down:
	sudo docker-compose down
term:
	docker exec -it -w /home/app cocotb /bin/bash
sim:
	docker run -w /home cocotb make -C $(SIM_DIRS)


clean:
	sudo docker image prune -f
	sudo docker volume prune -f

remove:
	sudo docker rmi -f cocotob
	sudo docker volume rm cocotob
