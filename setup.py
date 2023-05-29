#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Written by Lucas Sinclair.
MIT Licensed.
Contact at www.sinclair.bio
"""

# Imports #
from setuptools import setup, find_namespace_packages
from os import path

# Load the contents of the README file #
this_dir = path.abspath(path.dirname(__file__))
readme_path = path.join(this_dir, 'README.md')
with open(readme_path, encoding='utf-8') as handle: readme = handle.read()

# Call setup #
setup(
      name             = 'bumphub',
      version          = '1.2.1',
      description      = 'Scripts to automate distribution and packaging of'
                         ' python modules on PyPI and conda ',
      license          = 'MIT',
      url              = 'http://github.com/xapple/bumphub/',
      author           = 'Lucas Sinclair',
      author_email     = 'lucas.sinclair@me.com',
      install_requires = ['plumbing>=2.10.5', 'autopaths>=1.5.0',
                          'sh', 'rich', 'twine', 'pdoc', 'grayskull',
                          'conda-build'],
      python_requires  = ">=3.8",
      scripts          = ['pybump', 'anacondabump'],
      long_description = readme,
      long_description_content_type = 'text/markdown',
      include_package_data = True,
)