
generate: ## run the SDK generator
	$(info [+] Running SDK package generator...)
	python3 docker_generate.py
.PHONY: generate

test:
	python3 -m unittest discover -s tests/
.PHONY: test
