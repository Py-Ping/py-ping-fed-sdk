# Python Ping Fed SDK

Python based SDK generator for the Ping Federation API. This repository contains the scripts to build a Python module that can interface with the Ping Federate service API using the Python scripting language. Given a `VERSION` value the package can generate a version of the SDK that works with that version of Ping Federate. Currently this repository supports the following versions of Ping Federate 9.3.3, 10.0.4, 10.1.0, 10.2.1 and 11.0.0. The SDK generator can be tested with edge and latest versions of Ping Federate but no warranty is provided to guarantee this will work.

# Setup

To work with the SDK generator there are two ways you can work with the licensed Ping product:

1. This module is built off of the back of the `ping-devops` tool made available [here](https://devops.pingidentity.com/get-started/getStarted/). To run your own local development version of the Federate server follow all the steps from the prior link. On completion you will have the following environment variables which should be present in your local profile:

```
PING_IDENTITY_DEVOPS_USER
PING_IDENTITY_DEVOPS_KEY
PING_IDENTITY_DEVOPS_REGISTRY
PING_IDENTITY_DEVOPS_TAG
```

`PING_IDENTITY_DEVOPS_USER` and `PING_IDENTITY_DEVOPS_KEY` are available upon request [here](https://bit.ly/ping-devops-request).

2. If you have a license for the product put it in the root of the project directory with the name `pingfederate.lic`. This will then be mounted into the container used for SDK generation and will allow the product to be worked with.

# Pre-reqs (workspace setup, packages etc.)

 - `echo edge > PINGVERSION`

If running on alpine linux:
 - `apk add build-base libffi-dev`

If running on MacOS:
 - `brew install sphinx-doc`

# Installation

If pipenv module isn't installed yet:
```bash
pip3 install pipenv
```
Once pipenv has been installed and added to the PATH:
```bash
pipenv install
```

# Regenerate SDK

To regenerate the APIs and models of the SDK

```bash
export PING_IDENTITY_SWAGGER_URL= https://<pf_hostname>:<pf_admin_port>/pf-admin-api/v1/swagger.json
export PING_IDENTITY_SWAGGER_VERSION=<1.2/2.0>
make generate
```

This requires an available Ping Federate admin server instance with a set of credentials for access.

For a controlled generation of the Federate SDK we recommend using the dockerised version of the service. To do this install docker on your local host, update the content of the `PINGVERSION` file to the desired Federate version for the SDK and execute:

```bash
make docker-generate
```

This will download the Federate docker image from dockerhub, create a controlled running container with the Federate service running and then the SDK will be generated against that service host.

# Testing

A set of testing commands are available to assert that the generated SDK hasn't had any obvious issues in the generation process. If the version you wish to test is not supported by the generator but you'd like to test generation of the new version to add to the supported list modify the argument choices at the top of `docker_generate.py` and go through the testing steps to verify it's possible to be supported for generation.

To verify the version of the Fed SDK generated built successfully the following steps can shake out errors in a controlled fashion.

To run the unit tests use

```bash
make unittest
```

The unit tests will indicate any obvious issues in the generator itself. Make sure the `pingfedsdk` package folder is deleted otherwise this can have unexpected consequences to the unit test run session. If errors are discovered raise an issue in the github project.

To check the code coverage for the unit tests

```bash
make coverage
```

To lint the generator code, confirm it still follows PEP8 standards and the coding logic is still sound

```bash
make lint
```

To lint the generated code and confirm it still follows PEP8 standards

```bash
make lint-generated
```

This command will also indicate if there were any errors in the generation process against a version and is worthwhile for debugging generation.

To confirm the modules generated can be dynamically loaded into memory without syntax or dependency issues

```bash
make module-load-test
```

To load the Java integration kit and run some sample SDK commands to exercise the generated code

```bash
make example_<version>
```

Each version will have it's own example file which demonstrates SDK execution for the version of Ping Federate.

# Regenerate Documents

To regenerate the documents, after the generation of the SDK has been performed do the following.

```bash
cd docs
make html
```
