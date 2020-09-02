# Python Ping Fed SDK

Python based SDK for the Ping Federation API.
Contains data modules and API interactions


# Setup

This module is built off of the back of the `ping-devops` tool made available [here](https://pingidentity-devops.gitbook.io/devops/getstarted). To run your own local development version of the Federate server follow all the steps from the prior link. On completion you will have the following environment variables which should be present in your local profile:

```
PING_IDENTITY_DEVOPS_USER
PING_IDENTITY_DEVOPS_KEY
PING_IDENTITY_DEVOPS_REGISTRY
PING_IDENTITY_DEVOPS_TAG
```

`PING_IDENTITY_DEVOPS_USER` and `PING_IDENTITY_DEVOPS_KEY` are available upon request [here](https://bit.ly/ping-devops-request).


# Installation

```bash
# git clone this repo - something you've probably already done
pip install .
# OR python setup.py install
```

# Regenerate SDK

To regenerate the APIs and models of the SDK

```bash
make generate
```

This requires an available Ping Federate admin server instance with a set of credentials for access, to do this against a dockerised version of Ping Federate run the following:

```bash
make docker-generate
```

# Testing

A set of testing commands are available to assert that the generated SDK hasn't had any obvious issues in the generation process.

To run the unit tests use

```bash
make unittest
```

To check the code coverage for the unit tests

```bash
make coverage
```

To lint the generator code and confirm it still follows PEP8 standards

```bash
make lint
```

To lint the generated code and confirm it still follows PEP8 standards

```bash
make lint-generated
```

To confirm the modules generated can be dynamically loaded into memory without syntax or dependency issues

```bash
make module-load-test
```

To load the Java integration kit and run some sample SDK commands to exercise the generated code

```bash
make example
```

# Regenerate Documents

To regenerate the documents, after the generation of the SDK has been performed do the following.

```bash
cd docs
make html
```
