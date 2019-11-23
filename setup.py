#!/usr/bin/env python
# coding: utf-8
"""
   File Name: setup.py
      Author: Wan Ji
      E-mail: wanji@live.com
  Created on: Sat Jul  1 15:34:35 2017 CST
 Description:
"""


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='implor',
      version='0.4.2',
      author='WAN Ji',
      author_email='wanji@live.com',

      scripts=[
          'scripts/implor.py',
          'scripts/run_implor',
      ],
      url='http://github.com/wanji/implor',
      license='LICENSE',
      description='Image Explorer',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",

      install_requires=[
          "flask",
      ],
      )
