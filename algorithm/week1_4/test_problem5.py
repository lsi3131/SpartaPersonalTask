import itertools
import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120836

def solution(n):
    count = 0
    for i in range(1, n + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            count += 1

    return count


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(6, solution(20))
        self.assertEqual(9, solution(100))


if __name__ == '__main__':
    unittest.main()
