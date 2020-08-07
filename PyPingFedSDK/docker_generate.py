
import docker
import traceback
import os
import logging

from generate import Generate
from time import sleep


class ContainedGenerator:
    """
        Manager class for the SDK generator, encapsulates the process in a docker
        container such that there is no external dependency on a live pingfederate
        instance

        TODO: make generic to run any other Ping solution
    """

    def __init__(self, swagger_url, home_path, user, pass_key):
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p"
        )
        self.swagger_url = swagger_url
        self.logger = logging.getLogger("PingDSL.Docker")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))

        self.client = docker.from_env()
        self.image_name = "pingidentity/pingfederate:edge"
        self.home = home_path
        self.ping_user = user
        self.ping_key = pass_key

        self.container = None

    def run(self):
        self.container = self.client.containers.run(
            self.image_name,
            environment=[
                "PING_IDENTITY_ACCEPT_EULA=YES",
                f"PING_IDENTITY_DEVOPS_USER={self.ping_user}",
                f"PING_IDENTITY_DEVOPS_KEY={self.ping_key}",
                f"PING_IDENTITY_DEVOPS_HOME={self.home}/projects/devops",
                "PING_IDENTITY_DEVOPS_REGISTRY=docker.io/pingidentity",
                "PING_IDENTITY_DEVOPS_TAG=edge",
                "SERVER_PROFILE_URL=https://github.com/pingidentity/pingidentity-server-profiles.git",
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
        while self.container.status != "running" and \
              self.container.status != "exited" and \
              self.container.status != "paused":
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

    def generate(self):
        """
            Check to see if the ping fed container is running, if not run it and
            block until the container is available. Once available, generate the
            SDK from the swagger coming from the Ping Federate service. Once
            done, terminate the running container.

            TODO: wait on availability of running service
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

        try:
            Generate(self.swagger_url).generate()
        except Exception:
            self.logger.error(traceback.format_exc())

        self.logger.info("Terminating container...")
        self.terminate()


if __name__ == "__main__":
    home = os.environ["HOME"]
    ping_user = os.environ["PING_IDENTITY_DEVOPS_USER"]
    ping_key = os.environ["PING_IDENTITY_DEVOPS_KEY"]
    swagger_url = "https://localhost:9999/pf-admin-api/v1/api-docs"
    ContainedGenerator(
        swagger_url, home, ping_user, ping_key
    ).generate()
