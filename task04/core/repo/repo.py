from abc import ABC, abstractmethod
from domain import *


class GameResultRepository(ABC):
    @abstractmethod
    def save(self, result: GameResult):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def filter_by_result(self, results: list):
        pass

    @abstractmethod
    def filter_by_max_count(self, max_count: int):
        pass
