import os.path
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="hashed-cron",
    version="0.2.0",
    description="Utility library to convert Hashed Crons, using 'H' character.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/thiagowig/hashed-cron",
    author="Thiago Fonseca",
    author_email="dev.thiago@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=False,
)
