#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
import guess

def bin2str(binary):
    return ''.join(map(lambda c: '%x' % (ord(c)), binary))

class GuessTest(unittest.TestCase):


    def file_test(self, filename, expect):
        filepath = os.path.dirname(__file__) + '/' + filename
        f = open(filepath, 'r')
        for line in f:
            word = line.decode('UTF-8').rstrip()
            if word.startswith('#'):
                continue
            if expect == 'Shift_JIS':
                binary = word.encode('CP932')
            else:
                binary = word.encode(expect)
            detect = guess.guess(binary)
            if detect != expect:
                msg = '%s encode to %s by %s, but guess %s(%s)' \
                    % (word, bin2str(binary), expect, \
                           detect, binary.decode(detect))
                raise AssertionError(msg)

    def test_name6_UTF8(self):
        self.file_test('name6.txt', 'UTF-8')

    def test_name6_Shift_JIS(self):
        self.file_test('name6.txt', 'Shift_JIS')

    def test_name6_EUCJP(self):
        self.file_test('name6.txt', 'EUC-JP')

    def test_name6_ISO2022JP(self):
        self.file_test('name6.txt', 'ISO-2022-JP')

    def test_name5_UTF8(self):
        self.file_test('name5.txt', 'UTF-8')

    def test_name5_Shift_JIS(self):
        self.file_test('name5.txt', 'Shift_JIS')

    def test_name5_EUCJP(self):
        self.file_test('name5.txt', 'EUC-JP')

    def test_name5_ISO2022JP(self):
        self.file_test('name5.txt', 'ISO-2022-JP')

    def test_001_name_UTF8(self):
        self.file_test('test-name.txt', 'UTF-8')

    def test_002_name_Shift_JIS(self):
        self.file_test('test-name.txt', 'Shift_JIS')

    def test_003_name_EUCJP(self):
        self.file_test('test-name.txt', 'EUC-JP')

    def test_004_name_ISO2022JP(self):
        self.file_test('test-name.txt', 'ISO-2022-JP')

    def test_011_number_UTF8(self):
        self.file_test('test-number.txt', 'UTF-8')

    def test_012_number_Shift_JIS(self):
        self.file_test('test-number.txt', 'Shift_JIS')

    def test_013_number_EUCJP(self):
        self.file_test('test-number.txt', 'EUC-JP')

    def test_014_number_ISO2022JP(self):
        self.file_test('test-number.txt', 'ISO-2022-JP')

    def test_021_special_UTF8(self):
        self.file_test('test-special.txt', 'UTF-8')

    def test_022_special_Shift_JIS(self):
        self.file_test('test-special.txt', 'Shift_JIS')

if __name__ == '__main__':
    unittest.main()
