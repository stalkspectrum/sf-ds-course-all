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


def game_cycle(secret_num: int, print_out=True) -> int:
    ''' Отгадывает загаданное "секретное" число и подсчитывает число попыток.
        Для угадывания используется алгоритм бинарного поиска.

    Arguments:
        secret_num -- "Секретное" загаданное целое число

    Keyword Arguments:
        print_out -- Опционально для наглядности выводит на консоль пробные
            числа, загаданное число и общее количество попыток (default: {True})

    Returns:
        Общее количество попыток
    '''    
    probe_score = 0
    probe_range = GUESS_RANGE.copy()

    ##### while probe_range[1] - probe_range[0] > 1:
    while True:
        probe_score += 1
        probe_num = sum(probe_range) // 2
        if secret_num < probe_num:
            probe_range[1] = probe_num
        elif secret_num > probe_num:
            probe_range[0] = probe_num
        else:
            break
        if print_out:
            print(f'Пробуем угадать {probe_num} в диапазоне {probe_range}')

    if print_out:
        print(f'Загаданное число было: {secret_num}, попыток: {probe_score}')
    return probe_score


if __name__ == '__main__':
    #####game_cycle(secret_number(), print_out=True)
    for num_ in range(1, 101):
        game_cycle(num_, print_out=True)
        keypressed = input('Продолжаь?')