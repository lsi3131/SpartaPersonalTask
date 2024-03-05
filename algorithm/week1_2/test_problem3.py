import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120854

def solution(strlist):
    return [len(s) for s in strlist]


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([2, 3, 3, 6], solution(['We', 'are', 'the', 'world!']))
        self.assertEqual([1, 4, 12], solution(['I', 'Love', 'Programmers.']))


if __name__ == '__main__':
    unittest.main()
