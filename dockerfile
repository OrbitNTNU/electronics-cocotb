FROM python:3.9.18-bullseye

ADD modules /home/modules
WORKDIR /home/
RUN apt-get update
RUN apt-get -y install make python3 python3-pip verilog
RUN pip install cocotb
