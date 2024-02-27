from enum import Enum

RCP_TYPE_ROCK = 0
RCP_TYPE_SCISSOR = 1
RCP_TYPE_PAPER = 2

GAME_RESULT_WIN = 0
GAME_RESULT_LOSE = 1
GAME_RESULT_DRAW = 2

LANGUAGE_TYPE_ENG = 0
LANGUAGE_TYPE_KOR = 1

g_rcp_string_map = {
    RCP_TYPE_ROCK: ["rock", "바위"],
    RCP_TYPE_SCISSOR: ["scissor", "가위"],
    RCP_TYPE_PAPER: ["paper", "보"],
}

g_game_result_string_map = {
    GAME_RESULT_WIN: ['Win', '승리'],
    GAME_RESULT_LOSE: ['Lose', '패배'],
    GAME_RESULT_DRAW: ['Draw', '비김'],
}


def to_string_rcp(rcp_type, language) -> str:
    index = int(language)

    return g_rcp_string_map[rcp_type][index]


def to_string_game_result(game_result_type: int, language) -> str:
    index = int(language)

    return g_game_result_string_map[game_result_type][index]
