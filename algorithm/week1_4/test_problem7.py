import itertools
import unittest
import random
import string

# https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(mystring, n):
    s = ''
    for ch in mystring:
        s += ch * n
    return ''.join(s)


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual('hhheeellllllooo', solution('hello', 3))


if __name__ == '__main__':
    unittest.main()
