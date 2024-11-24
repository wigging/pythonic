help:
	@printf "\nCommands:\n"
	@printf "\033[32mcheck\033[0m   ruff linter and formatter checks\n"
	@printf "\033[32mclean\033[0m   delete cache directories\n"
	@printf "\033[32mtest\033[0m    run unit tests with pytest\n"
	@printf "\033[32mall\033[0m     run check, test, and clean rules\n"

check:
	ruff check .
	ruff format --check .

clean:
	rm -rf .ruff_cache
	rm -rf .pytest_cache
	rm -rf __pycache__

test:
	pytest --verbose --cache-clear

all: check test clean
