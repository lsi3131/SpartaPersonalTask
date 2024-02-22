import sys
import random
from enum import Enum


class UpDownType(Enum):
    UP = 1
    DOWN = 2
    MATCH = 3


def check_num(actual: int, expect: int):
    if actual < expect:
        return UpDownType.DOWN
    elif actual > expect:
        return UpDownType.UP
    else:
        return UpDownType.MATCH


def find_num_loop(actual: int):
    logs = []
    while True:
        num_str = input('숫자를 입력하세요 (1~100) : ')
        num = int(num_str)
        if num not in range(1, 100 + 1):
            print(f'입력값(={num})은 유효한 범위 내의 숫자가 아닙니다. 유효한 범위 내의 숫자(1, 100)을 입력하세요')
            continue

        result = check_num(actual, num)
        if result == UpDownType.DOWN:
            logs.append((actual, num, 'Down'))
            print('다운')
        elif result == UpDownType.UP:
            logs.append((actual, num, 'Up'))
            print('업')
        else:
            logs.append((actual, num, 'Match'))
            print('맞았습니다')
            break

    return logs


def run_game(argv):
    while True:
        generated_num = random.randint(1, 100)
        logs = find_num_loop(generated_num)
        print(f'시도한 횟수 : {len(logs)}')

        while True:
            result = input('다시 하시겠습니까? (y/n) : ')
            if result.lower() in ['y', 'n']:
                break

        if result == 'n':
            break

    print('게임을 종료합니다')


if __name__ == '__main__':
    run_game(sys.argv)
