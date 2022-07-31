#!/usr/bin/python3

sample1 = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."
sample2 = "Fibonacci numbers are strongly related to the golden ratio: Binet's formula expresses the nth Fibonacci number in terms of n and the golden ratio, and implies that the ratio of two consecutive Fibonacci numbers tends to the golden ratio as n increases."


def wordcount(string_in):
    alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
    dict_out = {letter: 0 for letter in alphabet_str}
    string_in = string_in.lower().replace('\'', '').replace('\"', '')
    list_cnt = string_in.split()
    for word in list_cnt:
        key = word[0]
        if key in dict_out:
            dict_out[key] += 1
    return dict_out


# print(wordcount(sample1))
# print(wordcount(sample2))
