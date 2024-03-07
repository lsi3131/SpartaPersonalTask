import unittest
import random
import string


# https://school.programmers.co.kr/learn/courses/30/lessons/120826

def solution(my_string: str, letter):
    data = []
    for ch in my_string:
        if ch not in letter:
            data.append(ch)

    return ''.join(data)


class TestProblem(unittest.TestCase):
    def test_example1(self):
        self.assertEqual('abcde', solution('abcdef', 'f'))
        self.assertEqual('Cdbe', solution('BCBdbe', 'B'))


if __name__ == '__main__':
    unittest.main()
