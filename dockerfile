FROM python:3.9.18-bullseye

ADD app /home/app
WORKDIR /home/app
RUN apt-get update
RUN apt-get -y install make python3 python3-pip
RUN pip install cocotb
