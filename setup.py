#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension
from os import path

setup(name = "guess",
      version = "1.0.2",
      description = "Gauche's charactor encoding detector for Python",
      long_description = '''
Example:

>>> import guess
>>> s = '\\xe3\\x81\\x82'
>>> print s
あ
>>> print guess.guess(s)
UTF-8
''',
      author = "Tsukasa Hamano",
      author_email = "code@cuspy.org",
      url="https://github.com/hamano/python-guess",
      download_url="http://pypi.python.org/pypi/guess/",
      license="BSD",
      ext_modules = [
        Extension(
            "guess",
            ["pyguess.c", "guess.c"],
            )
        ],
      classifiers = [
        'Natural Language :: Japanese',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      )
