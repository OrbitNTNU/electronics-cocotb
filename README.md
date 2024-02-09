# electronics-cocotb

## Introduction

This repository contains a testbench framework built using Python and cocotb (Coroutine based Cosimulation TestBench). The testbench is encapsulated within a Docker container for easy deployment and reproducibility.

## Requirements
- Docker: To run the testbench within the container.
- Docker Compose
- GNU Make

## Getting Started
To get started with the testbench, follow these steps:

1. Clone this repository to your local machine.
    ```bash
    git clone <repository_url>
    ```
2. Navigate to the repository directory.
    ```bash
    cd <repository_name>
    ```
3. Place the module that you want to test in the module folder. 
Note that the folder structure must look like the following:
```
modules/
--> <module>
----> rtl
----> sim
```
    
4. Run the Docker container from the makefile, which in turn runs cocotb inside the container
```bash
make sim
```

## Project Structure
- `modules/`: Directory for placing modules under test
- `makefile`: A Makefile is provided for convenience to build the Docker image and run the container.
- `Dockerfile`: Dockerfile which acts as a blueprint for the Docker container
- `docker-compose.yml`: Docker compose file for setting up container and volumes

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
