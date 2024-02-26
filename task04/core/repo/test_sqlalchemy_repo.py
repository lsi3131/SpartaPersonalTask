import datetime
import os.path
import unittest
import sqlalchemy_repo

from flask import Flask
from sqlalchemy_repo import *
from task04.core.repo.domain import GameResult


class Test(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.basedir = os.path.abspath(os.path.dirname(__file__))
        self.dbname = 'test_database.db'
        self.test_dbpath = os.path.join(self.basedir, self.dbname)

        if os.path.exists(self.test_dbpath):
            os.remove(self.test_dbpath)

    def tearDown(self):
        pass

    def test_db_file_should_deleted(self):
        self.assertFalse(os.path.exists(self.test_dbpath))

    def test_create_sqlalchemy_sqlite(self):
        db = create_sqlalchemy_sqlite(self.app, self.basedir, self.dbname)
        self.assertIsNotNone(db)

    def test_save_and_find_all(self):
        db = create_sqlalchemy_sqlite(self.app, self.basedir, self.dbname)
        repo = SQLAlchemyGameResultRepository(db)

        dt1 = datetime(2024, 1, 1, 0, 0, 30)
        dt2 = datetime(2024, 2, 1, 0, 0, 20)
        dt3 = datetime(2024, 3, 1, 0, 0, 10)
        save_datas = [
            GameResult(id=1, user='paper', computer='scissor', result='lose', game_datetime=dt1),
            GameResult(id=2, user='rock', computer='scissor', result='win', game_datetime=dt2),
            GameResult(id=3, user='paper', computer='paper', result='draw', game_datetime=dt3),
        ]

        for d in save_datas:
            repo.save(d)

        self.assertEqual(save_datas, repo.find_all())

    def test_convert(self):
        dt1 = datetime(2024, 1, 1, 0, 0, 0)
        from_alch = GameResultAlchemy(id=1, user='paper', computer='scissor', result='lose', game_datetime=dt1)
        to_data = convert_to_data(from_alch)

        self.assertEqual(GameResult(id=1, user='paper', computer='scissor', result='lose', game_datetime=dt1), to_data)

    def test_filter_by_result(self):
        db = create_sqlalchemy_sqlite(self.app, self.basedir, self.dbname)
        repo = SQLAlchemyGameResultRepository(db)

        dt1 = datetime(2024, 1, 1, 0, 0, 30)
        save_datas = [
            GameResult(id=1, user='paper', computer='scissor', result='lose', game_datetime=dt1),
            GameResult(id=2, user='rock', computer='scissor', result='win', game_datetime=dt1),
            GameResult(id=3, user='paper', computer='paper', result='draw', game_datetime=dt1),
        ]

        for d in save_datas:
            repo.save(d)

        self.assertEqual([save_datas[0]], repo.filter_by_result(['lose']))
        self.assertEqual([save_datas[1]], repo.filter_by_result(['win']))
        self.assertEqual([save_datas[2]], repo.filter_by_result(['draw']))

        self.assertEqual([save_datas[0], save_datas[1]], repo.filter_by_result(['lose', 'win']))
        self.assertEqual([save_datas[0], save_datas[2]], repo.filter_by_result(['lose', 'draw']))
        self.assertEqual([save_datas[1], save_datas[2]], repo.filter_by_result(['win', 'draw']))

        self.assertEqual(save_datas, repo.filter_by_result(['win', 'draw', 'lose']))

    def test_filter_by_max_count(self):
        db = create_sqlalchemy_sqlite(self.app, self.basedir, self.dbname)
        repo = SQLAlchemyGameResultRepository(db)

        dt1 = datetime(2024, 1, 1, 0, 0, 30)
        for d in range(1, 21):
            game_result = GameResult(id=d, user='paper', computer='scissor', result='lose', game_datetime=dt1)
            repo.save(game_result)


        self.assertEqual(0, len(repo.filter_by_max_count(0)))
        self.assertEqual(5, len(repo.filter_by_max_count(5)))
        self.assertEqual(20, len(repo.filter_by_max_count(30)))


if __name__ == '__main__':
    unittest.main()
