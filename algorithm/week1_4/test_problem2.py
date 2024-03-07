import itertools
import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120889

def solution(sides):
    sides.sort()
    return 1 if sides[0] + sides[1] > sides[2] else 2
    # return n * (2 ** k)


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(2, solution([1, 2, 3]))
        self.assertEqual(2, solution([3, 6, 2]))
        self.assertEqual(1, solution([199, 72, 222]))


if __name__ == '__main__':
    unittest.main()
