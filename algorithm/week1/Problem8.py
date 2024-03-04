import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120802

def solution(num1, num2):
    return num1 + num2


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(5, solution(2, 3))
        self.assertEqual(102, solution(100, 2))


if __name__ == '__main__':
    unittest.main()
