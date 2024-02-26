import random
import sys
from enum import Enum


class FightResult(Enum):
    WIN = 1
    LOSE = 2
    DRAW = 3
    INVALID = 4


WIN_LIST = [
    ('rock', 'scissor'),
    ('scissor', 'paper'),
    ('paper', 'rock'),
]

LOSE_LIST = [
    ('rock', 'paper'),
    ('scissor', 'rock'),
    ('paper', 'scissor'),
]

DRAW_LIST = [
    ('rock', 'rock'),
    ('scissor', 'scissor'),
    ('paper', 'paper'),
]

ROCK_SCISSOR_PAPER = ['rock', 'scissor', 'paper']

g_logs = []


def to_default_language(word: str):
    word_dictionary = [
        (['rock', '바위'], 'rock'),
        (['scissor', '가위'], 'scissor'),
        (['paper', '보'], 'paper')
    ]
    for from_words, to_word in word_dictionary:
        if word.lower() in from_words:
            return to_word
    return ''


def to_kor(word: str):
    word_dictionary = [
        (['rock'], '바위'),
        (['scissor'], '가위'),
        (['paper'], '보')
    ]
    for from_words, to_word in word_dictionary:
        if word.lower() in from_words:
            return to_word

    return word


def fight(user: str, computer: str):
    comp = (user, computer)
    if comp in WIN_LIST:
        return FightResult.WIN
    if comp in LOSE_LIST:
        return FightResult.LOSE
    if comp in DRAW_LIST:
        return FightResult.DRAW

    return FightResult.INVALID


def fight_loop(computer_choice: str):
    log = []
    while True:
        user_choice = input('가위(scissor), 바위(rock), 보(paper) 중 하나를 입력하세요 : ')
        user_choice_default = to_default_language(user_choice)
        if len(user_choice_default) == 0:
            print(f'입력값(={user_choice})은 유효한 입력이 아닙니다.')
            continue

        print(f'사용자: {to_kor(user_choice_default)}, 컴퓨터: {to_kor(computer_choice)}')
        result = fight(user_choice_default, computer_choice)
        if result == FightResult.WIN:
            print('사용자 승리')
        elif result == FightResult.LOSE:
            print('컴퓨터 승리')
        else:
            print('비김')

        log = (user_choice, computer_choice, result)
        break

    return log


def run_game(argv):
    while True:
        computer_choice = random.choice(ROCK_SCISSOR_PAPER)
        log = fight_loop(computer_choice)

        g_logs.append(log)

        while True:
            result = input('다시 하시겠습니까? (y/n) : ')
            if result.lower() in ['y', 'n']:
                break

        if result == 'n':
            break

    win_count = sum(1 for _, _, result in g_logs if result == FightResult.WIN)
    lose_count = sum(1 for _, _, result in g_logs if result == FightResult.LOSE)
    draw_count = sum(1 for _, _, result in g_logs if result == FightResult.DRAW)

    print(f'승: {win_count} 패: {lose_count}, 무승부: {draw_count}')
    print(g_logs)
    print('게임을 종료합니다')


if __name__ == '__main__':
    run_game(sys.argv)
