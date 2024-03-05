import collections
import unittest
import collections
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120822

def solution(my_string):
    return my_string[::-1]


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual('noraj', solution('jaron'))
        self.assertEqual('daerb', solution('bread'))


if __name__ == '__main__':
    unittest.main()
