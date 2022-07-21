#!/usr/bin/python3

""" Задание 8.8
    Написать программу, которая выводит на экран фразу в формате:
    Hello, <name>! Today is <dayofweek>. Have a nice day!
    Пример: Hello, John! Today is Friday. Have a nice day!
    Информация о пользователе содержится в следующих переменных:
        name - имя пользователя
        dayofweek - название дня недели
    Обязательное условие - задача должна быть решена с использованием метода
    format (Codeboard не поддерживает f-строки, поэтому приходится использовать
    метод format())
"""
name = 'John'
dayofweek = 'Friday'
print('Hello, {}! Today is {}. Have a nice day!'.format(name, dayofweek))
