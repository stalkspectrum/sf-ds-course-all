#!/usr/bin/python3

import game as g_

GAME_CYCLES = 1000


def average_score(game_cycles: int=1) -> float:
    """ Возвращает вычисленное среднее значение количества попыток
        угадывания числа в игре из модуля game.py.
    Аргументы:
        game_cycles -- Число вызываемых игровых циклов, по которым
        производится усреднение (default: 1).
    """
    probes_sum = 0
    for iteration in range(game_cycles):
        probes_sum += g_.game_cycle(g_.secret_number())
    return probes_sum / game_cycles


if __name__ == '__main__':
    print(f'Среднее число попыток за {GAME_CYCLES} игр:\n',
          f'    {average_score(GAME_CYCLES)}', sep='')
