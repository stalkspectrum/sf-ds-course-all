#!/usr/bin/python3

msample1 = [
            [1, 2, 3],
            [2, 3, 4],
            [5, 6, 7]
           ]
msample2 = [
            [2, 3, 4],
            [4, 5, 6],
            [4, 3, 2]
           ]


def matrix_sum(mx1, mx2):
    if len(mx1) != len(mx2) or len(mx1[0]) != len(mx2[0]):
        print('Error! Matrices dimensions are different!')
        return None
    mx_sum = []
    for row in range(len(mx1)):
        mx_sum.append([])
        for col in range(len(mx1[0])):
            mx_sum[row].append(mx1[row][col] + mx2[row][col])
    return mx_sum


print(matrix_sum(msample1, msample2))
# [
# [3, 5, 7],
# [6, 8, 10],
# [9, 9, 9]
# ]
