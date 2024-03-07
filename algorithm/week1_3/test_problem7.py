import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120824

def solution(num_list):
    odd, even = 0, 0
    for n in num_list:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    return [even, odd]


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([2, 3], solution([1, 2, 3, 4, 5]))
        self.assertEqual([0, 4], solution([1, 3, 5, 7]))


if __name__ == '__main__':
    unittest.main()
