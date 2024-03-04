import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120820

def solution(num1, num2):
    return divmod(num1, num2)[0]


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(2, solution(10, 5))
        self.assertEqual(3, solution(7, 2))


if __name__ == '__main__':
    unittest.main()
