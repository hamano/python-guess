#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension
from os import path

setup(name = "guess",
      version = "1.0.3",
      description = "Gauche's charactor encoding detector for Python",
      long_description = '''
Example:

>>> import guess
>>> s = '\\x82\\xa0\\x82\\xa2\\x82\\xa4\\x82\\xa6\\x82\\xa8'
>>> guess.guess(s)
'Shift_JIS'
>>> print s.decode('Shift_JIS')
あいうえお
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
