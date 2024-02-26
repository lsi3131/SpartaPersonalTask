import collections
import unittest
import random
import string
import re
import hashlib
from collections import *


class TestUpdown(unittest.TestCase):
    def test_example(self):
        password1 = '1234'
        encoded1 = hashlib.sha256(password1.encode()).hexdigest()

        password2 = '1234'
        encoded2 = hashlib.sha256(password2.encode()).hexdigest()

        self.assertEqual(encoded1, encoded2)


if __name__ == '__main__':
    unittest.main()
