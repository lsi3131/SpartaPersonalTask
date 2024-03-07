import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120814

def solution(n):
    count, remain = divmod(n, 7)
    if remain > 0:
        count += 1
    return count


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1, solution(7))
        self.assertEqual(3, solution(15))


if __name__ == '__main__':
    unittest.main()
