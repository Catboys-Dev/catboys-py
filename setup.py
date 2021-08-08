import re

from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = ''
with open('catboys/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)


requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


if not version:
    raise RuntimeError('version is not set')


setup(
    name='catboys',
    author='Kristian Kramer',
    author_email='kristian@catboys.com',
    url='https://github.com/Catboys-Dev/catboys-py',
    version=version,
    packages=['catboys'],
    license='GNU v3',
    description='A Python module that uses the Catboys API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=requirements
)
