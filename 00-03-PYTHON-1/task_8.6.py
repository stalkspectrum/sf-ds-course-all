#!/usr/bin/python3

""" Задание 8.6
    Написать небольшую программу, которая реализует ввод произвольного
    количества чисел через пробел и выводит эти же самые числа построчно.
"""
num_str = input('Enter some numbers separated by space: ')
num_list = num_str.split()
print('\n'.join(num_list))
