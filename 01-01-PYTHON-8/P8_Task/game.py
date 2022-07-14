#!/usr/bin/python3

import numpy as np

GUESS_RANGE = [1, 100]


def secret_number() -> int:
    ''' Загадывает "секретное" число в заданном диапазоне.
    Arguments:
        guess_range -- заданный диапазон в виде списка из двух целых чисел
            (включительно)
    Returns:
        "Секретное" загаданное целое число
    '''    
    return np.random.randint(GUESS_RANGE[0], GUESS_RANGE[1] + 1)


def game_cycle(secret_num: int, output=True) -> int:
    probe_score = 0
    probe_range = GUESS_RANGE.copy()
    while probe_range[1] - probe_range[0] > 1:
        probe_score += 1
        probe_num = sum(probe_range) // 2
        if output:
            print(f'Пробуем угадать {probe_num}')
        if secret_num < probe_num:
            probe_range[1] = probe_num
        elif secret_num > probe_num:
            probe_range[0] = probe_num
        else:
            break
    if output:
        print(f'Загаданное число было: {secret_num}, попыток: {probe_score}')
    return probe_score


if __name__ == '__main__':
    game_cycle(secret_number(), output=True)
