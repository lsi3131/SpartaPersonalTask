import datetime
import os.path
import unittest

from sqlalchemy_repo import *
from task04.core.config import AppConfig
from task04.core.definitions import *
from task04.core.domain import GameResult


class TestIntegration(unittest.TestCase):
    def setUp(self):
        dbname = 'test_database.db'
        self.config = AppConfig(__name__, os.path.abspath(os.path.dirname(__file__)), dbname)

        if os.path.exists(self.config.dbpath):
            os.remove(self.config.dbpath)

    def tearDown(self):
        if os.path.exists(self.config.dbpath):
            os.remove(self.config.dbpath)

    def test_db_file_should_deleted(self):
        self.assertFalse(os.path.exists(self.config.dbpath))

    def test_save_and_find_all(self):
        repo = self.config.game_result_repository()

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

    def test_convert(self):
        dt1 = datetime(2024, 1, 1, 0, 0, 0)
        from_alch = GameResultAlchemy(id=1, user=RCP_TYPE_PAPER, computer=RCP_TYPE_SCISSOR, result=GAME_RESULT_LOSE,
                                      game_datetime=dt1)
        to_data = convert_to_data(from_alch)

        self.assertEqual(GameResult(id=1, user=RCP_TYPE_PAPER, computer=RCP_TYPE_SCISSOR, result=GAME_RESULT_LOSE,
                                    game_datetime=dt1), to_data)

    def test_filter_by_result(self):
        repo = self.config.game_result_repository()

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
        repo = self.config.game_result_repository()

        dt1 = datetime(2024, 1, 1, 0, 0, 30)
        for d in range(1, 21):
            game_result = GameResult(id=d, user=RCP_TYPE_PAPER, computer=RCP_TYPE_SCISSOR, result=GAME_RESULT_LOSE,
                                     game_datetime=dt1)
            repo.save(game_result)

        self.assertEqual(0, len(repo.filter_by_max_count(0)))
        self.assertEqual(5, len(repo.filter_by_max_count(5)))
        self.assertEqual(20, len(repo.filter_by_max_count(30)))

    def test_keyargs(self):
        def func_kargs(**kargs):
            value = kargs.get('key')
            return value

        self.assertEqual('test', func_kargs(key='test'))
        self.assertEqual(None, func_kargs(not_key='test'))

    def test_slicing(self):
        data = [1, 2, 3, 4, 5]

        self.assertEqual([1, 2, 3], data[0:3])
        self.assertEqual([1, 2], data[0:2])


if __name__ == '__main__':
    unittest.main()
