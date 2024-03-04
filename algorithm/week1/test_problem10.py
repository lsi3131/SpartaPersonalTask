import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120829

def solution(n):
    return sum([d for d in range(2, n + 1, 2)])


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(6, solution(4))
        self.assertEqual(30, solution(10))


if __name__ == '__main__':
    unittest.main()
