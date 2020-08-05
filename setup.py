
from setuptools import setup, find_packages

requires = ["requests", "Jinja2", "PyYAML"]

setup(
    name="pypingsdk",
    version="0.1",
    description="Python Ping SDK",
    url="https://github.com/Versent/python-ping-federation-sdk",
    author="ProServ",
    author_email="support@versent.com.au",
    license="proprietary",
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=requires,
    zip_safe=False,
)