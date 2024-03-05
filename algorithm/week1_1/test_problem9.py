import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120829

def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4
    else:
        assert False


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1, solution(70))
        self.assertEqual(2, solution(90))
        self.assertEqual(3, solution(91))
        self.assertEqual(4, solution(180))


if __name__ == '__main__':
    unittest.main()
