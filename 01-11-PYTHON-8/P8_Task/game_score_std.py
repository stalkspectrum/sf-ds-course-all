#!/usr/bin/python3

import game_std as g_

GAME_CYCLES = 1000


def average_score(game_cycles: int=1) -> float:
    """ Возвращает вычисленное среднее арифметическое количества попыток
        угадывания числа в игре из модуля game_std.py.
    Аргументы:
        game_cycles -- Число вызываемых игровых циклов, по которым
            производится усреднение (default: 1).
    """
    probes_sum = 0
    for cycle in range(game_cycles):
        probes_sum += g_.game_cycle(g_.GUESS_RANGE)
    return probes_sum / game_cycles


if __name__ == '__main__':
    print(f'Среднее число попыток за {GAME_CYCLES} игр:\n',
          f'    {average_score(GAME_CYCLES)}', sep='')
