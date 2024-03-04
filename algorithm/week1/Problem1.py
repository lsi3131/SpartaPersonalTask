import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120803

def solution(num1, num2):
    return num1 - num2


class TestProblem2(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(-1, solution(2, 3))
        self.assertEqual(98, solution(100, 2))


if __name__ == '__main__':
    unittest.main()
