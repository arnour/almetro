#!/usr/bin/env python
from setuptools import find_packages, setup

project = "almetro"
version = "0.1.0"

setup(
    name=project,
    version=version,
    description="A python library to measure algorithms execution time and compare with its theoretical complexity",
    author="Arnour Sabino",
    author_email="arnour.sabino@gmail.com",
    url="https://github.com/arnour/almetro",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    setup_requires=[
        "nose>=1.3.7",
    ],
    dependency_links=[
    ],
    entry_points={
    },
    extras_require = {
        "test": [
            "flake8>=3.7.7",
            "flake8-print>=3.1.0",
            "coverage>=4.5.3",
            "PyHamcrest>=1.9.0",
        ],
    },
)
