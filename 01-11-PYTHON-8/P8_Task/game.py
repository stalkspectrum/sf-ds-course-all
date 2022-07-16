#!/usr/bin/python3

import numpy as np

GUESS_RANGE = [1, 100]


def secret_number() -> int:
    ''' Загадывает "секретное" число из диапазона, заданного в глобальной
        переменной GUESS_RANGE.
    Возвращает:
        "Секретное" загаданное целое число
    '''    
    return np.random.randint(GUESS_RANGE[0], GUESS_RANGE[1] + 1)


def game_cycle(secret_num: int, need_print=False) -> int:
    ''' Основной игровой цикл. Компьютер отгадывает им же загаданное
        "секретное" число и подсчитывает число попыток. Используется алгоритм
        бинарного поиска.
    Аргументы:
        secret_num -- "Секретное" загаданное целое число
    Именованные аргументы:
        need_print -- Опционально (полезно при непосредственном запуске
            программы, а не при импорте, как модуля) для наглядности выводит на
            консоль пробные числа, загаданное число и общее количество попыток
            (default: False)
    Возвращает:
        Общее количество попыток
    '''    
    probe_count = 0
    probe_range = GUESS_RANGE.copy()
    
    while True:
        probe_count += 1
        probe_num = sum(probe_range) // 2
        if secret_num < probe_num:
            probe_range[1] = probe_num
        elif secret_num > probe_num:
            probe_range[0] = probe_num
            if probe_range[1] - probe_range[0] == 1:
                probe_count += 1
                if need_print:
                    print(f'Угадали {probe_num + 1} в диапазоне {probe_range}')
                break
        else:
            if need_print:
                print(f'Угадали {probe_num} в диапазоне {probe_range}')
            break
        if need_print:
            print(f'Угадывали {probe_num}, меняем на {probe_range}')

    if need_print:
        print(f'Загаданное число было: {secret_num}, попыток: {probe_count}')
    return probe_count


if __name__ == '__main__':
    game_cycle(secret_number(), need_print=True)
    '''
    for num_ in range(GUESS_RANGE[0], GUESS_RANGE[1]+1):
        game_cycle(num_, need_print=True)
        keypressed = input('Продолжать?')
    '''
