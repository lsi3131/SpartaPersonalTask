import itertools
import unittest
import random
import string

# https://school.programmers.co.kr/learn/courses/30/lessons/120849

def solution(s):
    moums = list('aeiou')
    for m in moums:
        s = s.replace(m, '')

    return s


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual('bs', solution('bus'))


if __name__ == '__main__':
    unittest.main()
