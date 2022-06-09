#!/usr/bin/env python

import ast
import os
import re

from setuptools import (
    find_packages,
    setup,
)

SOURCE_DIR = "galaxy"

project_short_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
with open(f"{SOURCE_DIR}/project_galaxy_{project_short_name}.py") as f:
    init_contents = f.read()


def get_var(var_name):
    pattern = re.compile(rf"{var_name}\s+=\s+(.*)")
    match = pattern.search(init_contents)
    assert match
    return str(ast.literal_eval(match.group(1)))


version = get_var("__version__")
PROJECT_NAME = get_var("PROJECT_NAME")
PROJECT_URL = get_var("PROJECT_URL")
PROJECT_AUTHOR = get_var("PROJECT_AUTHOR")
PROJECT_EMAIL = get_var("PROJECT_EMAIL")
PROJECT_DESCRIPTION = get_var("PROJECT_DESCRIPTION")

PACKAGES = find_packages(where=".", exclude=["tests*"])
ENTRY_POINTS = """
        [console_scripts]
        gx-dump-tour=galaxy.selenium.scripts.dump_tour:main
"""
PACKAGE_DATA = {
    # Be sure to update MANIFEST.in for source dist.
    "galaxy": [
        "selenium/*yml",
    ],
}
PACKAGE_DIR = {
    SOURCE_DIR: SOURCE_DIR,
}

readme = open("README.rst").read()
history = open("HISTORY.rst").read()

if os.path.exists("requirements.txt"):
    requirements = open("requirements.txt").read().split("\n")
else:
    # In tox, it will cover them anyway.
    requirements = []

setup(
    name=PROJECT_NAME,
    version=version,
    description=PROJECT_DESCRIPTION,
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    url=PROJECT_URL,
    packages=PACKAGES,
    entry_points=ENTRY_POINTS,
    package_data=PACKAGE_DATA,
    package_dir=PACKAGE_DIR,
    include_package_data=True,
    install_requires=requirements,
    license="AFL",
    zip_safe=False,
    keywords="galaxy",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: Academic Free License (AFL)",
        "Operating System :: POSIX",
        "Topic :: Software Development",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Testing",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
