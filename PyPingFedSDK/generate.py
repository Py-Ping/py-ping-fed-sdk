import json
import os
import sys
import requests
import logging
from jinja2 import Environment, FileSystemLoader
from fetch import Fetch
from helpers import safe_name, requests_verb

class Generate():
    def __init__(self, api_schema_key='apis'):
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('PingDSL.Generate')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.api_schema_key = api_schema_key
        self.fetch_data = Fetch().fetch()

    def generate(self):
        for model, details in self.fetch_data.get('models').items():
            template = self.template('models', name=model, details=details)

            self.write_template(
                content=template,
                file_name=model,
                file_type='py',
                folder='models'
            )

        for api, details in self.fetch_data.get('apis').items():
            template = self.template('apis', name=api, details=details)

            self.write_template(
                content=template,
                file_name=api,
                file_type='py',
                folder='apis'
            )


    def template(self, template, name, details, template_directory='templates'):
        currentdirectory = os.path.dirname(__file__)
        templatedirectory = os.path.join(currentdirectory, template_directory)
        jinjaenvironment = Environment(
            loader=FileSystemLoader(templatedirectory),
            trim_blocks=True
        )
        jinjaenvironment.globals.update(safe_name=safe_name, requests_verb=requests_verb)
        jinjatemplate = jinjaenvironment.get_template(f'./{template}.j2')

        rendered_template = jinjatemplate.render(class_name=name, details=details)

        return rendered_template

    def write_template(self, content, file_name, file_type, folder='./apis'):
        filedirectory = os.path.dirname(os.path.realpath(__file__))
        targetdirectory = os.path.join(
            filedirectory,
            folder
        )

        if not os.path.exists(targetdirectory):
            os.makedirs(targetdirectory)

        path = f'{targetdirectory}/{file_name}.{file_type}'
        with open(os.path.join(filedirectory, path), "w") as fh:
            fh.write(content)


if __name__ == '__main__':
    Generate().generate()
