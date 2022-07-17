#!/usr/bin/python3

from random import randint

GUESS_RANGE = (1, 100)


def game_cycle(guess_range_: tuple=(1, 10),
               need_print=False) -> int:
    """ Основной игровой цикл. Компьютер отгадывает им же загаданное
        "секретное" число и подсчитывает число попыток. Используется
        адаптированный алгоритм бинарного поиска.
    Аргументы:
        guess_range_ -- Диапазон типа tuple для загадывания и
            отгадывания числа (default: [1, 10]).
    Именованные аргументы:
        need_print -- Опционально (полезно при непосредственном запуске
            программы, а не при импорте, как модуля) для наглядности
            выводит на консоль пробные числа, загаданное число и общее
            количество попыток (default: False).
    Возвращает:
        Общее количество попыток, затраченных на угадывание
        "секретного" числа.
    """
    # Загадываем "секретное" число
    secret_ = randint(*guess_range_)

    first_, last_ = guess_range_
    probe_count = 0

    while True:
        probe_count += 1
        probe_ = (first_ + last_) // 2
        if secret_ < probe_:
            last_ = probe_
        elif secret_ > probe_:
            first_ = probe_
            if last_ - first_ == 1:
                probe_count += 1
                if need_print:
                    print(f'Угадали {probe_ + 1} в интервале {first_}-{last_}')
                break
        else:
            if need_print:
                print(f'Угадали {probe_} в интервале {first_}-{last_}')
            break
        if need_print:
            print(f'Угадывали {probe_}, меняем интервал на {first_}-{last_}')

    if need_print:
        print(f'Загаданное число было: {secret_}, попыток: {probe_count}')
    return probe_count


if __name__ == '__main__':
    game_cycle(GUESS_RANGE, need_print=True)
