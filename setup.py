#!/usr/bin/env python

import setuptools

def slurp(infile_path, as_list=False):
    """Return lines of a file as a list or a string"""
    with open(infile_path, 'r') as infile:
        if as_list:
            all_contents = infile.readlines()
            return [line.strip() for line in all_contents if not line.startswith('#')]
        else:
            return infile.read()


setuptools.setup(name='py-ping-fed-sdk',
    version=slurp('VERSION'),
    description=slurp('description.txt'),
    author='ProServ',
    author_email='support@versent.com.au',
    license="proprietary",
    url="https://github.com/Versent/py-ping-fed-sdk",
    packages=setuptools.find_packages(exclude=["docs", "tests*"]),
    install_requires=slurp('requirements.txt', as_list=True),
    zip_safe=False,
)
