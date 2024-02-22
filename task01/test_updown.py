import collections
import unittest
import random
import string
import re
import updown
from updown import *
from collections import *


class TestUpdown(unittest.TestCase):
    def test_updown(self):
        self.assertEqual(UpDownType.MATCH, check_num(10, 10))
        self.assertEqual(UpDownType.DOWN, check_num(10, 5))
        self.assertEqual(UpDownType.UP, check_num(10, 15))

    def test_example(self):
        pass


if __name__ == '__main__':
    unittest.main()
