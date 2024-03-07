import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120903

def solution(s1, s2):
    count = 0
    for ch in s1:
        if ch in s2:
            count += 1

    return count


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(2, solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))


if __name__ == '__main__':
    unittest.main()
