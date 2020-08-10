# Python Ping Fed SDK

Python based SDK for the Ping Federation API.
Contains data modules and API interactions


# Setup

This module is built off of the back of the `ping-devops` tool made available [here](https://pingidentity-devops.gitbook.io/devops/getstarted). To run your own local development version of the Federate server follow all the steps from the prior link. One completion you will have the following environment variables which should be present in your local profile:

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


# Test

To run the unit tests use

```bash
make unittest
```


# Regenerate SDK

To regenerate the APIs and models of the SDK

```bash
make generate
```

