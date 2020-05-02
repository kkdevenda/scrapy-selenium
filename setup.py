# """This module contains the packaging routine for the pybook package"""

# from setuptools import setup, find_packages
# try:
#     from pip.download import PipSession
#     from pip.req import parse_requirements
# except ImportError:
#     # It is quick hack to support pip 10 that has changed its internal
#     # structure of the modules.
#     from pip._internal.download import PipSession
#     from pip._internal.req.req_file import parse_requirements


# def get_requirements(source):
#     """Get the requirements from the given ``source``

#     Parameters
#     ----------
#     source: str
#         The filename containing the requirements

#     """

#     install_reqs = parse_requirements(filename=source, session=PipSession())

#     return [str(ir.req) for ir in install_reqs]


# setup(
#     packages=find_packages(),
#     install_requires=get_requirements('requirements/requirements.txt')
# )

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scrapy-selenium", # Replace with your own username
    version="0.0.1",
    author="Krishna Kumar Devenda",
    author_email="kkdevenda@gmail.com",
    description="A scrapy middleware for Selenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkdevenda/scrapy-selenium.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

