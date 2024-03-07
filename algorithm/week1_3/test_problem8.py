import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120906

def solution(n):
    return sum(list(map(int, str(n))))


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(10, solution(1234))


if __name__ == '__main__':
    unittest.main()
