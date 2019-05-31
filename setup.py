import os
from setuptools import setup, find_packages


def _get_requirements(filename):
    """Return the requirements as a list of string."""
    requirements_path = os.path.join(os.path.dirname(__file__), filename)
    with open(requirements_path) as f:
        return f.readlines()

NAME: str = 'simple_package'
VERSION: str = '0.1.0'
DESCRIPTION: str = 'A simple python package.'

REQUIRES: list = _get_requirements('requirements.txt')
REQUIRES_DEV: list = _get_requirements('requirements-dev.txt')


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,

    zip_safe=False,

    install_requires=REQUIRES,

    packages=find_packages('src'),
    package_dir={'': 'src'},
    extras_require={"dev": REQUIRES_DEV}
)
