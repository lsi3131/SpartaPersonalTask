import datetime
import os.path
import unittest

from flask import Flask
from datetime import datetime

from service import *
from task04.core.sqlalchemy_repo import create_sqlalchemy_sqlite, SQLAlchemyGameResultRepository
from dateutil.relativedelta import relativedelta


class TestService(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.basedir = os.path.abspath(os.path.dirname(__file__))
        self.dbname = 'test_database.db'
        self.test_dbpath = os.path.join(self.basedir, self.dbname)

        if os.path.exists(self.test_dbpath):
            os.remove(self.test_dbpath)

        db = create_sqlalchemy_sqlite(self.app, self.basedir, self.dbname)
        self.service = GameService(SQLAlchemyGameResultRepository(db))
        self.dt_test = datetime(2020, 1, 1, 0, 0, 0)

    def tearDown(self):
        pass

    def test_fight(self):
        self.assertEqual(GAME_RESULT_DRAW, self.service.fight(RCP_TYPE_ROCK, RCP_TYPE_ROCK, datetime.now()).result)
        self.assertEqual(GAME_RESULT_WIN, self.service.fight(RCP_TYPE_ROCK, RCP_TYPE_SCISSOR, datetime.now()).result)
        self.assertEqual(GAME_RESULT_LOSE, self.service.fight(RCP_TYPE_ROCK, RCP_TYPE_PAPER, datetime.now()).result)

        self.assertEqual(GAME_RESULT_LOSE, self.service.fight(RCP_TYPE_SCISSOR, RCP_TYPE_ROCK, datetime.now()).result)
        self.assertEqual(GAME_RESULT_DRAW,
                         self.service.fight(RCP_TYPE_SCISSOR, RCP_TYPE_SCISSOR, datetime.now()).result)
        self.assertEqual(GAME_RESULT_WIN, self.service.fight(RCP_TYPE_SCISSOR, RCP_TYPE_PAPER, datetime.now()).result)

        self.assertEqual(GAME_RESULT_WIN, self.service.fight(RCP_TYPE_PAPER, RCP_TYPE_ROCK, datetime.now()).result)
        self.assertEqual(GAME_RESULT_LOSE, self.service.fight(RCP_TYPE_PAPER, RCP_TYPE_SCISSOR, datetime.now()).result)
        self.assertEqual(GAME_RESULT_DRAW, self.service.fight(RCP_TYPE_PAPER, RCP_TYPE_PAPER, datetime.now()).result)

    def test_fight_and_find_records(self):
        self.service.fight(RCP_TYPE_ROCK, RCP_TYPE_ROCK, self.dt_test)  # draw
        self.service.fight(RCP_TYPE_ROCK, RCP_TYPE_SCISSOR, self.dt_test)  # win
        self.service.fight(RCP_TYPE_ROCK, RCP_TYPE_PAPER, self.dt_test)  # lose

        records = self.service.find_game_records()
        self.assertEqual(3, len(records))
        self.assert_equal_without_id(GameResult(RCP_TYPE_ROCK, RCP_TYPE_ROCK, GAME_RESULT_DRAW, self.dt_test),
                                     records[0])
        self.assert_equal_without_id(GameResult(RCP_TYPE_ROCK, RCP_TYPE_SCISSOR, GAME_RESULT_WIN, self.dt_test),
                                     records[1])
        self.assert_equal_without_id(GameResult(RCP_TYPE_ROCK, RCP_TYPE_PAPER, GAME_RESULT_LOSE, self.dt_test),
                                     records[2])

    def test_find_record_reverse(self):
        dt1 = self.dt_test + relativedelta(months=1)
        dt2 = self.dt_test + relativedelta(months=2)
        dt3 = self.dt_test + relativedelta(months=3)
        self.service.fight(RCP_TYPE_ROCK, RCP_TYPE_ROCK, dt1)
        self.service.fight(RCP_TYPE_ROCK, RCP_TYPE_SCISSOR, dt2)
        self.service.fight(RCP_TYPE_ROCK, RCP_TYPE_PAPER, dt3)

        records = self.service.find_game_records(sort_option='game_datetime', reverse=True)
        self.assertEqual(3, len(records))
        self.assert_equal_without_id(GameResult(RCP_TYPE_ROCK, RCP_TYPE_PAPER, GAME_RESULT_LOSE, dt3),
                                     records[0])
        self.assert_equal_without_id(GameResult(RCP_TYPE_ROCK, RCP_TYPE_SCISSOR, GAME_RESULT_WIN, dt2),
                                     records[1])
        self.assert_equal_without_id(GameResult(RCP_TYPE_ROCK, RCP_TYPE_ROCK, GAME_RESULT_DRAW, dt1),
                                     records[2])

        pass

    def assert_equal_without_id(self, expect: GameResult, actual: GameResult):
        self.assertTrue(
            expect.user == actual.user and
            expect.computer == actual.computer and
            expect.result == actual.result and
            expect.game_datetime == actual.game_datetime)


if __name__ == '__main__':
    unittest.main()
