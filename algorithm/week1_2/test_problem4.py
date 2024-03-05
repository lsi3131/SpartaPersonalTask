import collections
import unittest
import collections
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120583

def solution(array, n):
    counter = collections.Counter(array)
    return counter[n]


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(2, solution([1, 1, 2, 3, 4, 5], 1))
        self.assertEqual(0, solution([0, 2, 3, 4], 1))


if __name__ == '__main__':
    unittest.main()
