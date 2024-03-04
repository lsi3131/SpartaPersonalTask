import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120820

def solution(age):
    return 2023 - age


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1983, solution(40))
        self.assertEqual(2000, solution(23))


if __name__ == '__main__':
    unittest.main()
