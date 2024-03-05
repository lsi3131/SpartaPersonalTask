import collections
import unittest
import collections
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120821

def solution(num_list):
    return num_list[::-1]


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([5, 4, 3, 2, 1], solution([1, 2, 3, 4, 5]))
        self.assertEqual([3, 2, 1], solution([1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
