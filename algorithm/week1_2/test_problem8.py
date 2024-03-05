import collections
import unittest
import collections
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120898

def solution(message):
    return len(message) * 2


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(30, solution('happy birthday!'))
        self.assertEqual(22, solution('I love you~'))


if __name__ == '__main__':
    unittest.main()
