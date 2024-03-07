import itertools
import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120851


def solution(s):
    result = 0
    for ch in s:
        if ch.isdigit():
            result += int(ch)
    return result


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(10, solution('aAb1B2cC34oOp'))


if __name__ == '__main__':
    unittest.main()
