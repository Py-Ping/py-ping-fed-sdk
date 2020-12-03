
import docker
import traceback
import os
import logging
import argparse

from helpers import get_auth_session, retry_with_backoff
from generate import Generate
from time import sleep

parser = argparse.ArgumentParser(description="PyLogger Generator")


def add_args():
    parser.add_argument(
        "version", type=str, choices=[
            "9.3.3",
            "10.0.4",
            "10.0.5",
            "10.0.6",
            "10.1.0",
            "10.1.1",
            "10.1.2",
            "edge"
        ],
        default="edge", help="Ping Federate Version"
    )


class Container:
    """
    Manager class for the SDK generator, encapsulates the process in a
    docker container such that there is no external dependency on a
    live ping federate instance

    TODO: make generic to run any other Ping solution
    """

    def __init__(self, home_path, user, pass_key, version="edge"):
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p"
        )
        self.logger = logging.getLogger("PingSDK.Docker")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))

        self.client = docker.from_env()
        self.image_name = f"pingidentity/pingfederate:{version}"
        self.home = home_path
        self.ping_user = user
        self.ping_key = pass_key
        self.version = version

        self.container = None

    def run(self):
        self.logger.info(f"Starting Container: {self.image_name}")
        self.container = self.client.containers.run(
            self.image_name,
            environment=[
                "PING_IDENTITY_ACCEPT_EULA=YES",
                f"PING_IDENTITY_DEVOPS_USER={self.ping_user}",
                f"PING_IDENTITY_DEVOPS_KEY={self.ping_key}",
                f"PING_IDENTITY_DEVOPS_HOME={self.home}/projects/devops",
                "PING_IDENTITY_DEVOPS_REGISTRY=docker.io/pingidentity",
                f"PING_IDENTITY_DEVOPS_TAG={self.version}",
                "SERVER_PROFILE_URL=https://github.com/"
                "pingidentity/pingidentity-server-profiles.git",
                "SERVER_PROFILE_PATH=getting-started/pingfederate"
            ],
            name="pingfederate",
            ports={"9031/tcp": 9031, "9999/tcp": 9999},
            detach=True
        )

    def terminate(self):
        """
        Perform post generation cleanup
        """
        self.container.stop()
        self.container.wait()
        self.container.remove()

    def get_by_image_name(self, image_name):
        """
        Given an image name, return the first available container object.
        """
        for container in self.client.containers.list():
            if container.image.tags[0] == image_name:
                return container

    def wait(self):
        """
        Block execution until the container is paused, exited or running.
        """
        while self.container.status not in ["running", "exited", "paused"]:
            self.container = self.client.containers.get(self.container.id)
            sleep(5)

    def running(self, image_name):
        """
        Given an image name, return if currently running
        """
        for container in self.client.containers.list():
            if container.image.tags[0] == image_name:
                return True
        return False

    def __enter__(self):
        """
        Enter method to setup a PingFed container
        """
        if not self.running(self.image_name):
            self.logger.info("Initialising Ping Federate container...")
            self.run()
            self.wait()
        else:
            self.container = self.get_by_image_name(self.image_name)

        # replace with something that polls on service availability
        sleep(45)
        self.logger.info("Container ready, generating SDK objects...")
        return self.container

    def __exit__(self, type, value, traceback):
        """
        Exit method to cleanup PingFed container when done
        """
        self.logger.info("Terminating container...")
        self.logger.debug("Terminating container...")
        self.terminate()


if __name__ == "__main__":
    add_args()
    args = parser.parse_args()
    home = os.environ["HOME"]
    ping_user = os.environ["PING_IDENTITY_DEVOPS_USER"]
    ping_key = os.environ["PING_IDENTITY_DEVOPS_KEY"]
    endpoint = "https://localhost:9999/pf-admin-api/v1"
    swagger_url = f"{endpoint}/api-docs"
    session = get_auth_session()
    session.verify = False

    with Container(home, ping_user, ping_key, args.version) as container:
        print(f'Running container {container.id}')
        if not retry_with_backoff(Generate(swagger_url).generate):
            print("Container service didn't stabilise, exiting...")
            exit(1)
        try:
            version = __import__("pingfedsdk.apis.version", fromlist=[""])
            response = version.Version(endpoint, session).getVersion()
            print(f"Ping Federate, version: {response.version}")
        except Exception as err:
            print(f"Was unable to determine the Ping Federate version: {err}")
            print(traceback.format_exc())
        finally:
            print("Ping Federation SDK Generation Finished")
