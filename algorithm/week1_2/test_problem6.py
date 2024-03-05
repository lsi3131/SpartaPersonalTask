import collections
import unittest
import collections
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120833

def solution(numbers, num1, num2):
    return numbers[num1:num2 + 1]


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([2, 3, 4], solution([1, 2, 3, 4, 5], 1, 3))
        self.assertEqual([3, 5], solution([1, 3, 5], 1, 2))
        self.assertEqual([3, 4, 5, 6], solution([1, 2, 3, 4, 5, 6, 7], 2, 5))


if __name__ == '__main__':
    unittest.main()
