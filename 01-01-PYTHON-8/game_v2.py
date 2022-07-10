#!/usr/bin/python3
''' Game "Guess a number from 1 to 100".
    Computer guesses.
'''
import numpy as np

def random_predict(number_: int=1) -> int:
    """ Computer guesses itself a number.
    Args:
        number_ (int, optional): Predicted number. Defaults to 1.
    Returns:
        int: number of attempts
    """    
    count_ = 0
    while True:
        count_ += 1
        predict_number_ = np.random.randint(1, 101)
        if number_ == predict_number_:
            break
    return(count_)


def score_game(random_predict) -> int:
    """_summary_
    Args:
        random_predict: The function defined above
    Returns:
        int: Average score of guess attempts
    """    
    count_list_ = []
    np.random.seed(1)
    random_array_ = np.random.randint(1, 101, size=(1000))
    for num_ in random_array_:
        count_list_.append(random_predict(num_))
    score_ = int(np.mean(count_list_))
    print(f'The algorithm guesses the number in {score_} attempts on average.')
    return score_


def main():
    ##### print(f'Attempts number: {random_predict(50)}')
    score_game(random_predict)


if __name__ == '__main__':
    main()
