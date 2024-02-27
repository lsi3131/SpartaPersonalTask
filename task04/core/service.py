from task04.core.domain import GameResult
from task04.core.repo import GameResultRepository
from task04.core.definitions import *

WIN_LIST = [
    (RCP_TYPE_ROCK, RCP_TYPE_SCISSOR),
    (RCP_TYPE_SCISSOR, RCP_TYPE_PAPER),
    (RCP_TYPE_PAPER, RCP_TYPE_ROCK),
]


class GameService:
    def __init__(self, repo: GameResultRepository):
        self.repo = repo

    def fight(self, user, computer, datetime) -> GameResult:
        if (user, computer) in WIN_LIST:
            game_result_type = GAME_RESULT_WIN
        elif user == computer:
            game_result_type = GAME_RESULT_DRAW
        else:
            game_result_type = GAME_RESULT_LOSE

        result = GameResult(
            user=user,
            computer=computer,
            result=game_result_type,
            game_datetime=datetime
        )

        self.repo.save(result)

        return result

    """
    sort_option
    - id[default]
    - datetime
    reverse
    - False - accending[default]
    - True - decending[default]
    
    """

    def find_game_records(self, reverse=False, sort_option='id', max_count=20, filtered_result=None) -> list[
        GameResult]:

        key_func = lambda x: x.id
        if sort_option == 'id':
            key_func = lambda x: x.id
        elif sort_option == 'user':
            key_func = lambda x: x.user
        elif sort_option == 'computer':
            key_func = lambda x: x.computer
        elif sort_option == 'result':
            key_func = lambda x: x.result
        elif sort_option == 'game_datetime':
            key_func = lambda x: x.game_datetime

        records = self.repo.find_all()
        if filtered_result and len(filtered_result) > 0:
            records = [r for r in records if r.result in filtered_result]

        records.sort(key=key_func, reverse=reverse)
        return records[0:max_count] if max_count >= 0 else records
