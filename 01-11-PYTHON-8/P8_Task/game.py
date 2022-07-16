#!/usr/bin/python3

import numpy as np

GUESS_RANGE = [1, 100]


def secret_number() -> int:
    """ Загадывает "секретное" число из диапазона, заданного в
        глобальной переменной GUESS_RANGE.
    Возвращает:
        "Секретное" загаданное целое число
    """
    return np.random.randint(GUESS_RANGE[0], GUESS_RANGE[1] + 1)


def game_cycle(secret_num: int, need_print=False) -> int:
    """ Основной игровой цикл. Компьютер отгадывает им же загаданное
        "секретное" число и подсчитывает число попыток. Используется
        алгоритм бинарного поиска.
    Аргументы:
        secret_num -- "Секретное" загаданное целое число
    Именованные аргументы:
        need_print -- Опционально (полезно при непосредственном запуске
            программы, а не при импорте, как модуля) для наглядности
            выводит на консоль пробные числа, загаданное число и общее
            количество попыток (default: False)
    Возвращает:
        Общее количество попыток
    """
    first_num = GUESS_RANGE[0]
    last_num = GUESS_RANGE[1]
    probe_count = 0
    
    while True:
        probe_count += 1
        probe_num = (first_num + last_num) // 2
        if secret_num < probe_num:
            last_num = probe_num
        elif secret_num > probe_num:
            first_num = probe_num
            if last_num - first_num == 1:
                probe_count += 1
                if need_print:
                    print(f'Угадали {probe_num + 1}',
                          f'в диапазоне {first_num}-{last_num}')
                break
        else:
            if need_print:
                print(f'Угадали {probe_num}',
                      f'в диапазоне {first_num}-{last_num}')
            break
        if need_print:
            print(f'Угадывали {probe_num},',
                  f'меняем диапазон на {first_num}-{last_num}')

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
