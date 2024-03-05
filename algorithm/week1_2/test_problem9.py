import collections
import unittest
import collections
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120841

def solution(dot):
    x, y = dot
    if x > 0 and y > 0:
        return 1
    if x < 0 < y:
        return 2
    if x < 0 and y < 0:
        return 3
    if x > 0 > y:
        return 4


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1, solution([2, 4]))
        self.assertEqual(2, solution([-7, 9]))


if __name__ == '__main__':
    unittest.main()
