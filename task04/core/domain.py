from dataclasses import dataclass
from datetime import datetime


@dataclass
class GameResult:
    user: int
    computer: int
    result: int
    game_datetime: datetime
    id: int = 0
