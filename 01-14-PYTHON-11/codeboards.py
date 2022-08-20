'''
Задание 2.3
Напишите функцию delete_columns(df, col=[]), которая удаляет столбцы из
DataFrame и возвращает новую таблицу. Если одного из указанных столбцов не
существует в таблице, то функция должна возвращать None.
Удалите выбранные вами столбцы из таблицы customer_df.
Подсказка
Для удаления столбцов используется метод drop() с параметром axis=1.
В него передаётся список столбцов, подлежащих удалению.
'''
import pandas as pd

def delete_columns(df, col=[]):
    if len(col) == 0:
        return None
    colset = set(col)
    if colset.issubset(set(df.columns)):
        newdf = df.drop(col, axis=1)
        return newdf
    else:
        return None


if __name__ == '__main__':
    customer_df = pd.DataFrame({
        'number': [0, 1, 2, 3, 4],
        'cust_id': [128, 1201, 9832, 4392, 7472],
        'cust_age': [13, 21, 19, 21, 60],
        'cust_sale': [0, 0, 0.2, 0.15, 0.3],
        'cust_year_birth': [2008, 2000, 2002, 2000, 1961],
        'cust_order': [1400, 14142, 900, 1240, 8430]
    })
    columns_for_delete= ['number', 'cust_id', 'cust_age']
    new_df = delete_columns(customer_df, columns_for_delete)
    print(new_df)
#   cust_sale  cust_year_birth  cust_order
# 0       0.00             2008        1400
# 1       0.00             2000       14142
# 2       0.20             2002         900
# 3       0.15             2000        1240
# 4       0.30             1961        8430


'''
Задание 2.4
Задан DataFrame countries_df, содержащий следующие столбцы: название страны (country),
население (population) в миллионах человек и площадь страны (square) в квадратных километрах.

import pandas as pd
countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})

Для каждой страны рассчитать плотность населения (количество человек на квадратный километр).
Затем по полученным данным рассчитать среднее по плотностям населения в указанных странах.

Население в таблице представлено в миллионах.
(Ответ округлить до сотых)
'''
density = countries_df['population'] * 1000000 / countries_df['square']
round(density.mean(), 2)
# 84.93
