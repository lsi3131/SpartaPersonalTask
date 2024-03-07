import itertools
import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120813

def solution(n):
    result = []
    for i in range(1, n + 1, 2):
        result.append(i)
    return result


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([1, 3, 5, 7, 9], solution(10))
        self.assertEqual([1, 3, 5, 7, 9, 11, 13, 15], solution(15))


if __name__ == '__main__':
    unittest.main()
