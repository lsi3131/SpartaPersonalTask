import collections
import unittest
import collections
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120908

def solution(str1, str2):
    return 1 if str2 in str1 else 2


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1, solution("ab6CDE443fgh22iJKlmn1o", "6CD"))
        self.assertEqual(2, solution("ppprrrogrammers", "pppp"))
        self.assertEqual(2, solution("AbcAbcA", "AAA"))


if __name__ == '__main__':
    unittest.main()
