# Makefile for building publishing container
PROJECT = pypingfedsdk
VERSION = $(shell whoami)
#AUTH = $(shell aws --profile build --region ap-southeast-2 secretsmanager get-secret-value --secret-id arn:aws:secretsmanager:ap-southeast-2:264748061542:secret:github/versent-builder-foTpJN | jq -r '.SecretString | fromjson | .OAuthKey')
PWD = $(shell pwd)
GITSHORTHASH = $(shell git rev-parse HEAD | cut -c 1-7)
GITSHORTHASH_AWS = $(shell echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
REGISTRY = local
APP_IMAGE = $(PROJECT):$(GITSHORTHASH)
APP_IMAGE_AWS = $(PROJECT):$(GITSHORTHASH_AWS)
CONTAINER_TAG = latest
REGION = ap-southeast-2
ACCOUNTID = 012345678901
REGISTRY = $(ACCOUNTID).dkr.ecr.$(REGION).amazonaws.com

genReqs:
	pipenv lock -r > requirements.txt
.PHONY: genReqs

genTestReqs:
	pipenv lock -r --dev > requirements.txt
.PHONY: genTestReqs

buildLocal: genReqs
	docker build -t $(APP_IMAGE) -f Dockerfile.alpine .
.PHONY: build

build: genReqs
	docker build -t $(APP_IMAGE_AWS) -f Dockerfile.ubuntu .
.PHONY: build

test: genTestReqs
	docker build -f Dockerfile.test -t $(PROJECT)-test .
.PHONY: test

ecrLogin:
	aws ecr get-login --no-include-email  --profile $(PROFILE) --region $(REGION) | bash
.PHONY: ecrLogin

ecrPush: ecrLogin
	docker tag $(APP_IMAGE) $(REGISTRY)/$(APP_IMAGE)
	docker tag $(APP_IMAGE) $(REGISTRY)/$(PROJECT):$(CONTAINER_TAG)
	docker push $(REGISTRY)/$(APP_IMAGE)
	docker push $(REGISTRY)/$(PROJECT):$(CONTAINER_TAG)
.PHONY: ecrPush

buildRequirements:
	pipenv lock -r > requirements.txt
.PHONY: buildRequirements

generate: ## run the SDK generator
	$(info [+] Running SDK package generator...)
	python3 PyPingFedSDK/generate.py
.PHONY: generate

docker-generate: ## run the SDK generator
	$(info [+] Running Dockerised SDK package generator...)
	python3 src/docker_generate.py
.PHONY: docker-generate

unittest:
	PYTHONPATH=$(shell pwd)/src/ python3 -m unittest discover -s tests/
.PHONY: unittest

coverage:
	PYTHONPATH=$(shell pwd)/src/ coverage run --branch -m unittest discover -s tests/ && coverage report --omit=/usr/lib/python3/dist-packages/*,tests/*
.PHONY: coverage

lint:
	flake8 --exclude */apis/*,*/models/*,*/source/*,*/enums.py,
.PHONY: lint