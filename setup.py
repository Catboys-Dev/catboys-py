import re

from setuptools import setup


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
    include_package_data=True,
    install_requires=requirements
)
