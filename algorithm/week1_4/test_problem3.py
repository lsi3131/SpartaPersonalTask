import itertools
import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120811

def solution(array):
    array.sort()
    right = len(array) - 1
    left = 0
    mid = left + (right - left) // 2
    return array[mid]


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(7, solution([1, 2, 7, 10, 7]))


if __name__ == '__main__':
    unittest.main()
