from dataclasses import dataclass
from datetime import datetime


@dataclass
class GameResult:
    user: str
    computer: str
    result: str
    game_datetime: datetime
    id: int = 0
