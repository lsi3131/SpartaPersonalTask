import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120585

def solution(array, height):
    tall_than_me_list = [a for a in array if a > height]
    return len(tall_than_me_list)


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(3, solution([149, 180, 192, 170], 167))
        self.assertEqual(0, solution([180, 120, 140], 190))


if __name__ == '__main__':
    unittest.main()
