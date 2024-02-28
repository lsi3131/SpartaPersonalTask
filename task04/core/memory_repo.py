from task04.core.domain import GameResult
from task04.core.repo import GameResultRepository


class MemoryGameResultRepository(GameResultRepository):
    def __init__(self):
        self.store = {}
        self.sequence = 0

    def save(self, result: GameResult):
        result.id = self.sequence
        self.sequence += 1
        self.store[result.id] = result
        return result

    def find_all(self) -> list[GameResult]:
        # key_func = lambda x: x.id

        return sorted(list(self.store.values()), key=lambda x: x.id)

    def filter_by_result(self, results: list):
        records = self.find_all()
        return [x for x in records if x.result in results]

    def filter_by_max_count(self, max_count: int):
        return self.find_all()[0:max_count]
