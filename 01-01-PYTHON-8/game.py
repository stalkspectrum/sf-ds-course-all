#!/usr/bin/python3
''' Game "Guess a number from 1 to 100".
    A player guesses.
'''
import numpy as np

number_ = np.random.randint(1, 101)
count_ = 0
while True:
    count_ += 1
    predict_number_ = int(input('Guess a number from 1 to 100: '))
    if predict_number_ > number_:
        print('No, the number is less.')
    elif predict_number_ < number_:
        print('No, the number is more')
    else:
        print(f'The number is guessed. That is equal to {number_} in {count_} attempts.')
        break
