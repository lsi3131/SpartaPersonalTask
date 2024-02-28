import os

from flask import Flask

from task04.core.memory_repo import MemoryGameResultRepository
from task04.core.service import GameService
from task04.core.sqlalchemy_repo import *


class AppConfig:
    def __init__(self, app_name, basedir_path, db_name):
        self.basedir_path = basedir_path
        self.dbname = db_name  # 추후 json등 설정 파일에서 읽어올것
        self.app = Flask(app_name)
        self.dbpath = os.path.join(self.basedir_path, self.dbname)

    def get_game_result_service(self) -> GameService:
        return GameService(self.game_result_repository())

    def game_result_repository(self) -> GameResultRepository:
        return self.__create_game_result_sqlalchemy_repo()
        # return MemoryGameResultRepository()

    def __create_game_result_sqlalchemy_repo(self):
        alchemy = create_sqlalchemy_sqlite(self.app, self.basedir_path, self.dbname)
        return SQLAlchemyGameResultRepository(alchemy)
