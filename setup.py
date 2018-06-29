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

try:
    from pypandoc import convert

    def read_md(fpath):
        return convert(fpath, 'rst')
except ImportError:
    print("warning: pypandoc module not found, DONOT convert Markdown to RST")

    def read_md(fpath):
        with open(fpath, 'r') as fp:
            return fp.read()

setup(name='implor',
      version='0.3.2',
      author='WAN Ji',
      author_email='wanji@live.com',

      scripts=[
          'scripts/implor.py',
          'scripts/run_implor',
      ],
      url='http://wanji.me/implor',
      license='LICENSE',
      description='Image Explorer',

      install_requires=[
          "flask",
      ],
      )
