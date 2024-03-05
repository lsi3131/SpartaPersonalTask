import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120804

def solution(num1, num2):
    return num1 * num2


class TestProblem2(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(12, solution(3, 4))
        self.assertEqual(513, solution(27, 19))


if __name__ == '__main__':
    unittest.main()
