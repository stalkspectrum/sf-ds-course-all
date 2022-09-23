'''
Задание 4.6
Предоставлен файл './Root/data/test_data.csv'.

one,two,three,four,five
1.331586504129518,0.7152789743984055,-1.5454002921112682,bar,
,,1.0,,
-0.008383849928522256,0.6213359738904805,-0.7200855607188968,bar,
1.0,0.5,0.5,,
0.2655115856921195,0.10854852571496944,0.004291430934033236,bar,yes
-0.17460021059294129,0.433026189953598,1.203037373812212,bar,
,,1.2,hist,
-0.9650656705167633,1.028274077982704,0.2286301301246597,bar,


Прочитав этот файл, получается вот такой DataFrame:

        one       two     three  four five
0  1.331587  0.715279 -1.545400   bar  NaN
1       NaN       NaN  1.000000   NaN  NaN
2 -0.008384  0.621336 -0.720086   bar  NaN
3  1.000000  0.500000  0.500000   NaN  NaN
4  0.265512  0.108549  0.004291   bar  yes
5 -0.174600  0.433026  1.203037   bar  NaN
6       NaN       NaN  1.200000  hist  NaN
7 -0.965066  1.028274  0.228630   bar  NaN

Задача - очистить данную таблицу от пропусков следующим образом:
- Если признак имеет больше 50 % пропущенных значений, удалите его.
- Для оставшихся данных: если в строке более двух пропусков, удалите строку.
- Для оставшихся данных: числовые признаки заполните средним значением, а
категориальные - модой.

Должна получиться следующая таблица df:
Рис2
'''
import pandas as pd

df = pd.read_csv('./Root/data/test_data.csv')

threshold1 = int(df.shape[0] * 0.5)
df.dropna(how='any', thresh=threshold1, axis='columns', inplace=True)

threshold2 = int(df.shape[1] - 2)
df.dropna(axis='index', thresh=threshold2, inplace=True)

values_dict = {
    'one': df['one'].mean(),
    'two': df['two'].mean(),
    'three': df['three'].mean(),
    'four': df['four'].mode()[0]
}
df.fillna(value=values_dict, inplace=True)


'''
Задание 6.1
Надо немного модифицировать функцию outliers_iqr().

def outliers_iqr(data, feature):
    x = data[feature]
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75)
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    return outliers, cleaned

Добавить в неё параметры left и right, которые задают число IQR влево и вправо
от границ ящика (пусть по умолчанию они равны 1.5). Функция, как и раньше,
должна возвращать потенциальные выбросы и очищенный DataFrame.
'''
import pandas as pd

def outliers_iqr_mod(data, feature, left=1.5, right=1.5):
    x = data[feature]
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75)
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * left)
    upper_bound = quartile_3 + (iqr * right)
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    return outliers, cleaned


'''
Задание 6.3
Надо расширить правило трёх сигм, чтобы иметь возможность особенности данных.

def outliers_z_score(data, feature, log_scale=False):
    if log_scale:
        x = np.log(data[feature] + 1)
    else:
        x = data[feature]
    mu = x.mean()
    sigma = x.std()
    lower_bound = mu - 3 * sigma
    upper_bound = mu + 3 * sigma
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    return outliers, cleaned

Добавить в функцию outliers_z_score() параметры left и right, которые будут
задавать число сигм (стандартных отклонений) влево и вправо соответственно,
определяющее границы метода z-отклонения. По умолчанию оба параметры равны 3.
Результирующую функцию назвать outliers_z_score_mod().
'''
import pandas as pd
import numpy as np

def outliers_z_score_mod(data, feature, log_scale=False, left=3, right=3):
    if log_scale:
        x = np.log(data[feature] + 1)
    else:
        x = data[feature]
    mu = x.mean()
    sigma = x.std()
    lower_bound = mu - left * sigma
    upper_bound = mu + right * sigma
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    return outliers, cleaned

