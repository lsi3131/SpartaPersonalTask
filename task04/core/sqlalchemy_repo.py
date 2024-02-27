import os

from flask import Flask
from sqlalchemy import desc

from task04.core.domain import *
from flask_sqlalchemy import SQLAlchemy

from task04.core.repo import GameResultRepository

g_db = SQLAlchemy()


class GameResultAlchemy(g_db.Model):
    id = g_db.Column(g_db.Integer, primary_key=True, autoincrement=True)
    user = g_db.Column(g_db.Integer, nullable=False)
    computer = g_db.Column(g_db.Integer, nullable=False)
    result = g_db.Column(g_db.Integer, nullable=False)
    game_datetime = g_db.Column(g_db.DateTime, nullable=True)

    def __repr__(self):
        return f'GameResult'


class SQLAlchemyWrapper:
    def __init__(self, db, app):
        self.db = db
        self.app = app


def create_sqlalchemy_sqlite(app: Flask, basedir: str, dbname: str) -> SQLAlchemyWrapper:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                            os.path.join(basedir, dbname)

    g_db.init_app(app)

    with app.app_context():
        g_db.create_all()

    return SQLAlchemyWrapper(g_db, app)


def convert_to_sqlalchemy(data: GameResult):
    # data.user
    return GameResultAlchemy(
        user=data.user,
        computer=data.computer,
        result=data.result,
        game_datetime=data.game_datetime
    )


def convert_to_data(a: GameResultAlchemy):
    return GameResult(
        id=a.id,
        user=a.user,
        computer=a.computer,
        result=a.result,
        game_datetime=a.game_datetime
    )


class SQLAlchemyGameResultRepository(GameResultRepository):
    def __init__(self, a: SQLAlchemyWrapper):
        self.db = a.db
        self.app = a.app

    def save(self, result: GameResult):
        with self.app.app_context():
            self.db.session.add(convert_to_sqlalchemy(result))
            self.db.session.commit()

    def find_all(self):
        with self.app.app_context():
            return [convert_to_data(a) for a in GameResultAlchemy.query.all()]

    def filter_by_result(self, results: list):
        with self.app.app_context():
            return [convert_to_data(a) for a in
                    GameResultAlchemy.query.filter(GameResultAlchemy.result.in_(results)).all()]

    def filter_by_max_count(self, max_count: int):
        if max_count <= 0:
            return []
        with self.app.app_context():
            return [convert_to_data(a) for a in
                    GameResultAlchemy.query.order_by(desc(GameResultAlchemy.game_datetime)).limit(max_count).all()]
