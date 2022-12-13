.SHELL := /usr/bin/bash
.PHONY: docs

BOLD=$(shell tput -T xterm bold)
MAGENTA=$(shell tput -T xterm setaf 5)
RESET=$(shell tput -T xterm sgr0)
DAY :=

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


fmt:
	@printf "\n${BOLD}${MAGENTA}***RUNNING FORMAT***${RESET}\n\n"
	black ./

lint:
	@printf "\n${BOLD}${MAGENTA}***RUNNING LINTER***${RESET}\n\n"
	flake8

day:
	mkdir aoc/$(DAY)
	cd aoc/$(DAY) && touch input.txt solution.py puzzle.txt solution-2.py