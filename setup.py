#!/usr/bin/env python

from setuptools import setup, find_packages

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name = "commands.py",
        version = "0.5",
        author = "AnotherTwinkle",
        url = "https://www.github.com/AnotherTwinkle/commands.py",
        packages = ["commands"],
        install_requires = requirements,
        include_package_data = True,
        )
        
