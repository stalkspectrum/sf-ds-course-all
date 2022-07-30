#!/usr/bin/python3

text_example = '''A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place.'''


def get_most_frequent_word(text_):
    punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
    for punct in punctuation_list:
        text_ = text_.replace(punct, '')
    word_list = text_.lower().split()
    word_dict = {}
    max_count = 0
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
        if word_dict[word] > max_count:
            max_count = word_dict[word]
            most_frequent_word = word
    return most_frequent_word


print(get_most_frequent_word(text_example))
