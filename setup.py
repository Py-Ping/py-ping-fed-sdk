#!/usr/bin/env python

from setuptools import setup


def read_contents(name):
    with open(name, "r") as fh:
        return fh.read()


requires = [
    'requests>=2.23.0,<2.24.0'
]


setup(
    name=f"pingfedsdk-{read_contents('PINGVERSION')}",
    version=read_contents("VERSION"),
    description=read_contents("DESCRIPTION"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 2 - Pre-Alpha",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operation System :: OS Independant",
    ],
    author="ProServ",
    author_email="support@versent.com.au",
    license="proprietary",
    url="https://github.com/Versent/py-ping-fed-sdk",
    py_modules=["pingfedsdk"],
    package_dir={"": "pingfedsdk"},
    install_requires=requires,
    zip_safe=False,
)
