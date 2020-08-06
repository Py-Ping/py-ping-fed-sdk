
from setuptools import setup, find_packages

requires = ["requests", "Jinja2", "PyYAML"]

setup(
    name="py-ping-fed-sdk",
    version="0.1",
    description="Python Ping Federation SDK",
    url="https://github.com/Versent/py-ping-fed-sdk",
    author="ProServ",
    author_email="support@versent.com.au",
    license="proprietary",
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=requires,
    zip_safe=False,
)