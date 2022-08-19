# -*- coding: utf-8 -*-
# @Time    : 2022/8/19 17:21
# @Author  : mollie
# @FileName: test.py
# @Software: PyCharm
import pytest

class Test01():

    def test_01(self):
        print('\n---用例01---')

    def test_02(self):
        print('\n---用例02---')

    def test_03(self):
        print('\n---用例03---')

if __name__ == '__main__':
    pytest.main(['-vs'])