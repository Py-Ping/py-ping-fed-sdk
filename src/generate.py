import os
import logging
from jinja2 import Environment, FileSystemLoader
from fetch import Fetch
from helpers import safe_name, safe_variable, json_type_convert, ref_type_convert


class Generate():
    def __init__(self, swagger_url, api_schema_key="apis"):
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("PingDSL.Generate")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.api_schema_key = api_schema_key
        self.fetch_data = Fetch(swagger_url).fetch()

    def generate(self):
        for model, details in self.fetch_data.get("models").items():
            template = self.render_file("models", name=model, details=details)
            self.write_template(
                content=template, file_name=model, file_type="py",
                folder="../PyPingFedSDK/models"
            )

        template = self.render_file(
            "models_doc", name="models_doc", details=self.fetch_data.get("models")
        )

        self.write_template(
            content=template,
            file_name="models",
            file_type="rst",
            folder="../docs/source/models"
        )

        enum_template = self.render_file(
            "enums", name="enums", details=self.fetch_data.get("enums")
        )
        self.write_template(
            content=enum_template, file_name="enums", file_type="py",
            folder="../PyPingFedSDK/"
        )

        for api, details in self.fetch_data.get("apis").items():
            template = self.render_file(
                "apis", name=safe_name(api), details=details
            )

            self.write_template(
                content=template,
                file_name=safe_name(api),
                file_type="py",
                folder="../PyPingFedSDK/apis"
            )

        template = self.render_file(
            "apis_doc", name="apis_doc", details=self.fetch_data.get("apis")
        )

        self.write_template(
            content=template, file_name="apis", file_type="rst",
            folder="../docs/source/apis"
        )

    def render_file(self, template, name, details, template_directory="templates"):
        """
            Given the name of the jinja2 template to work from, the name of the
            class being generated inside of the file, the data to fill in to the
            file with the template and the directory where the template resides
            render the code file and return the result as a string.
        """
        currentdirectory = os.path.dirname(__file__)
        templatedirectory = os.path.join(currentdirectory, template_directory)
        jinjaenvironment = Environment(
            loader=FileSystemLoader(templatedirectory),
            trim_blocks=True
        )
        jinjaenvironment.globals.update(
            safe_name=safe_name, safe_variable=safe_variable,
            json_type_convert=json_type_convert, ref_type_convert=ref_type_convert
        )
        jinjatemplate = jinjaenvironment.get_template(f"./{template}.j2")

        rendered_template = jinjatemplate.render(class_name=name, details=details)

        return rendered_template

    def write_template(self, content, file_name, file_type, folder="./apis"):
        """
        Given some content string, a file name and type and folder, write the
        content to disk in the required location.
        """
        filedirectory = os.path.dirname(os.path.realpath(__file__))
        targetdirectory = os.path.join(
            filedirectory,
            folder
        )

        if not os.path.exists(targetdirectory):
            os.makedirs(targetdirectory)

        path = f"{targetdirectory}/{file_name}.{file_type}"
        with open(os.path.join(filedirectory, path), "w") as fh:
            fh.write(content)


if __name__ == "__main__":
    Generate("https://localhost:9999/pf-admin-api/v1/api-docs").generate()
