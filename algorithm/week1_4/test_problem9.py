import itertools
import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120909

import math
def solution(n):
    n_sqrt = math.sqrt(n)
    not_sqrt = (n_sqrt - int(n_sqrt)) > 0
    return 2 if not_sqrt else 1


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1, solution(144))
        self.assertEqual(2, solution(976))


if __name__ == '__main__':
    unittest.main()
