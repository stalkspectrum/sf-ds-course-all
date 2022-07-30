#!/usr/bin/python3

text_example = ''"A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."''


def get_unique_words(text_):
    punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
    for punct in punctuation_list:
        text_ = text_.replace(punct, '')
    word_set = set(text_.lower().split())
    return sorted(list(word_set))


print(get_unique_words(text_example))
