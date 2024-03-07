import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120819

def solution(money):
    price = 5500
    count, remain = divmod(money, price)
    return [count, remain]


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([1, 0], solution(5500))
        self.assertEqual([2, 4000], solution(15000))


if __name__ == '__main__':
    unittest.main()
