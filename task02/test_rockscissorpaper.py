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
        self.assertEqual('rock', translate('바위'))
        self.assertEqual('scissor', translate('가위'))
        self.assertEqual('paper', translate('보'))

        self.assertEqual('rock', translate('rock'))
        self.assertEqual('scissor', translate('scissor'))
        self.assertEqual('paper', translate('paper'))

        self.assertEqual('paper', translate('PapeR'))
        self.assertEqual('rock', translate('RoCK'))
        self.assertEqual('scissor', translate('SciSSOR'))

    def test_example(self):
        pass


if __name__ == '__main__':
    unittest.main()
