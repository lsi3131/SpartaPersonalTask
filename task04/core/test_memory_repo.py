import datetime
import os.path
import unittest

from sqlalchemy_repo import *
from task04.core.config import AppConfig
from task04.core.definitions import *
from task04.core.domain import GameResult
from task04.core.memory_repo import MemoryGameResultRepository


class TestMemoryRepo(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_save_and_find_all(self):
        repo = MemoryGameResultRepository()

        dt1 = datetime(2024, 1, 1, 0, 0, 30)
        dt2 = datetime(2024, 2, 1, 0, 0, 20)
        dt3 = datetime(2024, 3, 1, 0, 0, 10)
        save_datas = [
            GameResult(id=1, user=RCP_TYPE_PAPER, computer=RCP_TYPE_SCISSOR, result=GAME_RESULT_LOSE,
                       game_datetime=dt1),
            GameResult(id=2, user=RCP_TYPE_ROCK, computer=RCP_TYPE_SCISSOR, result=GAME_RESULT_WIN, game_datetime=dt2),
            GameResult(id=3, user=RCP_TYPE_PAPER, computer=RCP_TYPE_PAPER, result=GAME_RESULT_DRAW, game_datetime=dt3),
        ]

        for d in save_datas:
            repo.save(d)

        self.assertEqual(save_datas, repo.find_all())

    def test_filter_by_result(self):
        repo = MemoryGameResultRepository()

        dt1 = datetime(2024, 1, 1, 0, 0, 30)
        save_datas = [
            GameResult(id=1, user=RCP_TYPE_PAPER, computer=RCP_TYPE_SCISSOR, result=GAME_RESULT_LOSE,
                       game_datetime=dt1),
            GameResult(id=2, user=int(RCP_TYPE_ROCK), computer=RCP_TYPE_SCISSOR, result=GAME_RESULT_WIN,
                       game_datetime=dt1),
            GameResult(id=3, user=RCP_TYPE_PAPER, computer=RCP_TYPE_PAPER, result=GAME_RESULT_DRAW, game_datetime=dt1),
        ]

        for d in save_datas:
            repo.save(d)

        self.assertEqual([save_datas[0]], repo.filter_by_result([GAME_RESULT_LOSE]))
        self.assertEqual([save_datas[1]], repo.filter_by_result([GAME_RESULT_WIN]))
        self.assertEqual([save_datas[2]], repo.filter_by_result([GAME_RESULT_DRAW]))

        self.assertEqual([save_datas[0], save_datas[1]], repo.filter_by_result([GAME_RESULT_LOSE, GAME_RESULT_WIN]))
        self.assertEqual([save_datas[0], save_datas[2]], repo.filter_by_result([GAME_RESULT_LOSE, GAME_RESULT_DRAW]))
        self.assertEqual([save_datas[1], save_datas[2]], repo.filter_by_result([GAME_RESULT_WIN, GAME_RESULT_DRAW]))

        self.assertEqual(save_datas, repo.filter_by_result([GAME_RESULT_WIN, GAME_RESULT_DRAW, GAME_RESULT_LOSE]))

    def test_filter_by_max_count(self):
        repo = MemoryGameResultRepository()

        dt1 = datetime(2024, 1, 1, 0, 0, 30)
        for d in range(1, 21):
            game_result = GameResult(id=d, user=RCP_TYPE_PAPER, computer=RCP_TYPE_SCISSOR, result=GAME_RESULT_LOSE,
                                     game_datetime=dt1)
            repo.save(game_result)

        self.assertEqual(0, len(repo.filter_by_max_count(0)))
        self.assertEqual(5, len(repo.filter_by_max_count(5)))
        self.assertEqual(20, len(repo.filter_by_max_count(30)))


if __name__ == '__main__':
    unittest.main()
