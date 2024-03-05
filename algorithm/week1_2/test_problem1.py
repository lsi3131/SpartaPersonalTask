import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120817

def solution(numbers):
    return sum(numbers) / len(numbers)


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(5.5, solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        self.assertEqual(94.0, solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))


if __name__ == '__main__':
    unittest.main()
