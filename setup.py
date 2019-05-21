from setuptools import setup, find_packages

NAME: str = 'simple_package'
VERSION: str = '0.1.0'
DESCRIPTION: str = 'A simple python package.'

REQUIRES: list = []


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,

    zip_safe=False,

    install_requires=REQUIRES,

    packages=find_packages('src'),
    package_dir={'': 'src'},
)
