import collections
import unittest
import random
import string
import re
import rockscissorpaper
from rockscissorpaper import *
from collections import *


class TestUpdown(unittest.TestCase):
    def test_fight(self):
        self.assertEqual(FightResult.DRAW, fight('rock', 'rock'))
        self.assertEqual(FightResult.WIN, fight('rock', 'scissor'))
        self.assertEqual(FightResult.LOSE, fight('rock', 'paper'))

        self.assertEqual(FightResult.LOSE, fight('scissor', 'rock'))
        self.assertEqual(FightResult.DRAW, fight('scissor', 'scissor'))
        self.assertEqual(FightResult.WIN, fight('scissor', 'paper'))

        self.assertEqual(FightResult.WIN, fight('paper', 'rock'))
        self.assertEqual(FightResult.LOSE, fight('paper', 'scissor'))
        self.assertEqual(FightResult.DRAW, fight('paper', 'paper'))

        self.assertEqual(FightResult.INVALID, fight('invalid1', 'paper'))

    def test_translate(self):
        self.assertEqual('rock', to_default_language('바위'))
        self.assertEqual('scissor', to_default_language('가위'))
        self.assertEqual('paper', to_default_language('보'))

        self.assertEqual('rock', to_default_language('rock'))
        self.assertEqual('scissor', to_default_language('scissor'))
        self.assertEqual('paper', to_default_language('paper'))

        self.assertEqual('paper', to_default_language('PapeR'))
        self.assertEqual('rock', to_default_language('RoCK'))
        self.assertEqual('scissor', to_default_language('SciSSOR'))

    def test_example(self):
        pass


if __name__ == '__main__':
    unittest.main()
