import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120809

def solution(numbers):
    return list(map(lambda x: x * 2, numbers))


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([2, 4, 6, 8, 10], solution([1, 2, 3, 4, 5]))
        self.assertEqual([2, 4, 200, -198, 2, 4, 6], solution([1, 2, 100, -99, 1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
