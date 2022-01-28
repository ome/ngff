#!/usr/bin/env python

import codecs
import os
from typing import List

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


install_requires: List[List[str]] = []
install_requires += (["jsonschema"],)


setup(
    name="ome-ngff",
    version="0.0.4dev",
    author="The Open Microscopy Team",
    url="https://github.com/ome/ngff",
    description="OME Next-Generation File Format: spec and schemas",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=["ome_ngff"],
    py_modules=["ome_ngff"],
    # include_package_data = True, 
    python_requires=">=3.6",
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
    ],
    tests_require=["pytest"],
)
