import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120816

def solution(slice, n):
    count, remain = divmod(n, slice)
    count += 1
    if remain == 0:
        count -= 1
    return count


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(2, solution(7, 10))
        self.assertEqual(3, solution(4, 12))


if __name__ == '__main__':
    unittest.main()
