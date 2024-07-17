DC := docker-compose
TEST_DC := docker-compose.test.yaml
env ?= test

ifeq ($(env),test)
    CURRENT_DC := $(TEST_DC)
else
    $(error Invalid value for env: $(env). Valid value is 'test'.)
endif


.PHONY: build
build:
	$(DC) -f $(CURRENT_DC) up --build

.PHONY: up
up:
	$(DC) -f $(CURRENT_DC) up

