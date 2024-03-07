import itertools
import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120818

def solution(price):
    if 500000 <= price:
        price *= (1 - 0.20)
    elif 300000 <= price < 500000:
        price *= (1 - 0.10)
    elif 100000 <= price < 300000:
        price *= (1 - 0.05)

    return int(price)


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(142500, solution(150000))
        self.assertEqual(464000, solution(580000))


if __name__ == '__main__':
    unittest.main()
