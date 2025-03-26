PHONY: test
test:
    @echo = 'tests started...'
    @set = PYTHONPATH=. &&pytest -m pytest -v


PHONY: check
check:
	echo '1234'
	black .
	isort .
	flake8 .
