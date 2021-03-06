import os
from setuptools import setup, find_packages


def _get_requirements(filename):
    """Return the requirements as a list of string."""
    requirements_path = os.path.join(os.path.dirname(__file__), filename)
    with open(requirements_path) as f:
        return f.readlines()


def read(file_path: str):
    """Simply return the content of a file."""
    with open(file_path) as f:
        return f.read()


NAME: str = "simple_package"
VERSION: str = "0.1.1"
DESCRIPTION: str = "A simple python package."

REQUIRES: list = _get_requirements("requirements.txt")
REQUIRES_DEV: list = _get_requirements("requirements-dev.txt")


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read(os.path.join(os.path.dirname(__file__), 'README.md')),
    long_description_content_type='text/markdown',
    zip_safe=False,
    install_requires=REQUIRES,
    packages=find_packages("src"),
    package_dir={"": "src"},
    extras_require={"dev": REQUIRES_DEV},
    entry_points={
        "console_scripts": [
            "now=simple_package.dates:now",
            "hour+1=simple_package.dates:plus_hour",
            "hour-1=simple_package.dates:minus_hour",
        ]
    },
)
