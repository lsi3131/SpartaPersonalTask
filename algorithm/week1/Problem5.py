import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120805

def solution(num1, num2):
    return divmod(num1, num2)[1]


class TestProblem2(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1, solution(3, 2))
        self.assertEqual(0, solution(10, 5))


if __name__ == '__main__':
    unittest.main()
