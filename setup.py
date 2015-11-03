#!/usr/bin/env python
from setuptools import setup

setup(
    name='skyrms',
    version='0.1',
    install_requires=['numpy', 'scipy'],
    description='Dynamic analysis of signaling games',
    author='Manolo Martínez',
    author_email='mail@manolomartinez.net',
    url='https://github.com/manolomartinez/signal',
    packages=['skyrms'],
    license='GPLv3'
)
