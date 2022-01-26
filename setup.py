#!/usr/bin/env python3

from setuptools import setup, find_packages

tests_require = ["pytest"]
linters_require = ["black>=20.8b1", "pylint", "flake8"]

setup(
    name="data_engineering_challenge",
    version="0.1",
    description="Complete the challenge",
    keywords="data",
    author="Simantini Shinde",
    license="CC0 1.0 Universal",
    install_requires=[
        "pandas",
    ],
    extras_require={"tests": tests_require, "linters": linters_require},
    packages=find_packages(),
    entry_points={"console_scripts": ["data_engineering_challenge = "
                                      "data_engineering_challenge.data_engineering:main"]},
    python_requires=">=3.6",
)
