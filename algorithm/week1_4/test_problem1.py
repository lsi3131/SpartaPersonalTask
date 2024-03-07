import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120910

def solution(n, k):
    return n * (2 ** k)


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(2048, solution(2, 10))
        self.assertEqual(229376, solution(7, 15))


if __name__ == '__main__':
    unittest.main()
