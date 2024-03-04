import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120807

def solution(num1, num2):
    return 1 if num1 == num2 else -1


class TestProblem2(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(-1, solution(2, 3))
        self.assertEqual(1, solution(11, 11))
        self.assertEqual(-1, solution(7, 99))


if __name__ == '__main__':
    unittest.main()
