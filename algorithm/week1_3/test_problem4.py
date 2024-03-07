import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120847

def solution(numbers):
    m_val = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            d = numbers[i] * numbers[j]
            if m_val < d:
                m_val = d

    return m_val


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(20, solution([1, 2, 3, 4, 5]))
        self.assertEqual(744, solution([0, 31, 24, 10, 1, 9]))


if __name__ == '__main__':
    unittest.main()
