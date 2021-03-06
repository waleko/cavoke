from enum import Enum, auto


class GameStatus(Enum):
    PLAYING = auto()
    WON = auto()
    LOST = auto()
    DRAW = auto()
    FINISHED = auto()
    UNKNOWN = auto()
