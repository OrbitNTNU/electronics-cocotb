.PHONY: all
SIM_DIRS := $(shell find modules -type d -name "sim")

all: sim

restart: down up
up:
	sudo docker-compose up -d
down:
	sudo docker-compose down
term:
	docker exec -it -w /home/ cocotb /bin/bash

sim: $(SIM_DIRS)

$(SIM_DIRS): up
	docker run -w /home cocotb make -C $@

clean:
	sudo docker image prune -f
	sudo docker volume prune -f
remove:
	sudo docker rmi -f cocotb
	sudo docker volume rm cocotb
