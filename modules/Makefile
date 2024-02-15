# Recursive make
.PHONY: all

# Find all directories named "sim" recursively
SIM_DIRS := $(shell find . -type d -name "sim")

# Define the targets
all: $(SIM_DIRS)

# Run make in each found directory
$(SIM_DIRS):
	@$(MAKE) -C $@
