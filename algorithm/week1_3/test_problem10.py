import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120830

def solution(n, k):
    sheep = 12000
    drink = 2000
    bonus, remain = divmod(n, 10)
    k -= bonus

    return sheep * n + drink * k


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(124000, solution(10, 3))


if __name__ == '__main__':
    unittest.main()
