## Задачи из юнитов модуля PYTHON-6 (Практика) ##

#### **Задание 1.8** ####

Написать функцию `change_password`, которая должна возвращать отформатированную
строку в следующем виде:    
`User user_name changed password to new_password`    
Уже есть заготовка функции&nbsp;&mdash; осталось только задать строку.
Переменные, которые надо использовать, указаны в круглых скобках после имени
функции (`user_name`&nbsp;&mdash; имя пользователя, `new_password`&nbsp;&mdash;
новый пароль).    
***Обязательное условие***    
Задача должна быть решена с использованием метода `format`.

```python
def change_password(user_name, new_password):
    return 'User {} changed password to {}'.format(user_name, new_password)
```

----

#### **Задание 2.5** ####

Написать функцию `get_unique_words()`, которая избавляется от знаков препинания
в тексте и возвращает упорядоченный список (слова расположены по алфавиту) из
уникальных (неповторяющихся) слов. Учесть, что слова, написанные в разных
регистрах считаются одним и тем же словом.
Можно использовать готовый список со знаками препинания:    
`punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']`    
Текст, который можно использовать в качестве примера:    
`text_example = """A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."""`

[**`task_2.5.py`**](task_2.5.py)

----

#### **Задание 2.6** ####

Модификация предыдущего задания.    
Необходимо написать функцию `get_most_frequent_word()`, которая возвращает самое
часто встречающееся слово в тексте. Не забудьте очистить тест от знаков
пунктуации и привести текст к единому регистру (слова в верхнем и нижнем
регистре считаются одним и тем же словом). Для решения можно использовать
функцию из предыдущего задания.

[**`task_2.6.py`**](task_2.6.py)

----

#### **Задание 2.7** ####

Разработать функцию `holes_count()`, которая подсчитывает количество отверстий в
заданном числе. Например, в цифре 8 два отверстия, в цифре 9&nbsp;&mdash; одно.
В числе 146 два отверстия.

```python
def holes_count(number):
    holes_num = 0
    number_str = str(number)
    for digit in number_str:
        if digit in ['4', '6', '9', '0']:
            holes_num += 1
        elif digit == '8':
            holes_num += 2
    return holes_num
```

----

#### **Задание 2.8** ####

Написать программу, которая запрашивает у пользователя следующие данные:
`username`, `age`, `email` о нескольких пользователях и собирает эти данные в
структуру:    

```text
[
    (1, {'username': user1, 'age': age1, 'email': email1}),
    (2, {'username': user2, 'age': age2, 'email': email2}),
    ...
]
```

Первый элемент каждого кортежа&nbsp;&mdash; порядковый номер пользователя,
второй элемент&nbsp;&mdash; словарь с данными. В итоге должен получиться список
с кортежами.    
Далее необходимо провести аналитику (собрать данные о пользователях в словарь)

```text
{
    'username': [user1, user2, ...],
    'age': [age1, age2, ...],
    'email': [email1, email2, ...]
}
```

и вывести эту аналитику на экран.

[**`task_2.8.py`**](task_2.8.py)

----

#### **Задание 3.4** ####

Написать функцию `find_min_number()`, которая принимает три числа на вход и
возвращает наименьшее из них. Использовать для решения задачи условия.

```python
def find_min_number(a, b, c):
    return a if (a < b and a < c)
             else (b if (b < a and b < c)
                     else c)
```

----

#### **Задание 3.5** ####

Усложнение предыдущей задачи.    
Написать функцию `sum_min_numbers()`, которая также принимает на вход три числа
и возвращает сумму двух наименьших. Можно использовать функцию из предыдущего
задания для поиска минимального числа.

```python
def sum_min_numbers(aa, bb, cc):
    def find_min_number(a, b, c):
        return a if a<b and a<c else (b if b<a and b<c else c)
    return find_min_number(aa+bb, aa+cc, bb+cc)
```

----

#### **Задание 3.6** ####

Написать функцию `is_divided_by_six()`, которая проверяет, делится ли число на
`6`. При решении воспользоваться тернарным оператором.    
Функция должна вернуть `True`, если число делится на `6`, и `False`&nbsp;&mdash;
в противном случае.    
***Подсказка***    
Число делится на `6`, если оно делится на `2` и на `3`.

```python
def is_divided_by_six(number):
    return (False, True)[number % 2 == 0 and number % 3 == 0]

# Simplified function
def keep_it_simple_stupid(number):
    return (False, True)[number % 6 == 0]
```

----

#### **Задание 3.7** ####

Написать функцию `check_number_sign()`, которая возвращает `1`, если число
положительное; `-1`, если число отрицательное; `0`, если число&nbsp;&mdash; `0`.
Функция принимает на вход одно число. Использовать в коде множественные
ветвления.

```python
def check_number_sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0
```

----

#### **Задание 3.8** ####

Написать функцию `division()`, которая осуществляет деление двух чисел.    
Необходимо реализовать внутри функции отлов исключения `ZeroDivisionError` на
случай, если пользователь при вызове функции попытается поделить на ноль.
Функция принимает на вход два числа&nbsp;&mdash; делимое и делитель, и
возвращает частное.    
Если в процессе выполнения функции было поймано исключение `ZeroDivisionError`,
то на экран нужно вывести сообщение:    
`'Error! Matrices dimensions are different!'`    
с помощью функции `print()`, а затем вернуть значение `None` из функции.

```python
def division(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        print('Error! Matrices dimensions are different!')
        return None
```

----

#### **Задание 4.4** ####

Написать функцию `lucky_ticket()`, которая проверяет, является ли билет
счастливым.    
***Примечание***    
Билет счастливый, если сумма первых трёх цифр равна сумме последних трёх цифр.    
На вход функция получает шестизначное число.

```python
def lucky_ticket(ticket_number):
    str1 = str(ticket_number[:3])
    str2 = str(ticket_number[3:])
    sum1 = 0
    sum2 = 0
    for sign in str1:
        sum1 += int(sign)
    for sign in str2:
        sum2 += int(sign)
    if sum1 == sum2:
        return True
    return False
```

----

#### **Задание 4.5** ####

Написать функцию `fib_number()`, которая получает на вход некоторое число `n` и
выводит `n`-e число Фибоначчи.    
Задачу можно решить как с помощью цикла `for`, так и с помощью цикла `while`.    
***Примечание 1***    
Числа Фибоначчи определяются так:    
`a0 = 0, a1 = 1, a2 = a1 + a0 = 1, an = a_n-1 + a_n-2`    
***Примечание 2***    
В модуле по функциям уже было задание на вычисление чисел Фибоначчи с помощью
рекурсивных функций. Здесь необходимо реализовать те же вычисления, но без
использования рекурсии.

```python
def fib_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        flist = [0, 1]
        fnum = 2
        while len(flist) < n + 1:
            flist.append(flist[fnum-1] + flist[fnum-2])
            fnum += 1
        return flist[-1]
```

----

#### **Задание 4.6** ####

Написать функцию `even_numbers_in_matrix()`, которая получает на вход матрицу
(список из списков) и возвращает количество чётных чисел в ней.

```python
matrix_sample = [
                  [1, 5, 4],
                  [4, 2, -2],
                  [7, 65, 88]
                 ]

def even_numbers_in_matrix(matrix):
    even_nums = 0
    for row in matrix:
        for col in row:
            if col % 2 == 0:
                even_nums += 1
    return even_nums


print(even_numbers_in_matrix(matrix_sample))
# 5
```

----

#### **Задание 4.7** ####

Написать функцию `matrix_sum()`, которая получает на вход две матрицы и
возвращает их сумму.    
***Примечание***    
Чтобы найти сумму двух матриц, нужно просуммировать их соответствующие элементы.
Но перед этим необходимо проверить, что размеры матриц одинаковы (одинаковое
количество столбцов и одинаковое количество строк). Если размеры матриц не
совпадают, то надо вывести на экран сообщение    
`'Error! Matrices dimensions are different!'`    
с помощью функции `print()`, а затем вернуть значение `None` из функции
`matrix_sum()`. Например:

```text
1 2 3   2 3 4   3 5 7
2 3 4 + 4 5 6 = 6 8 10
5 6 7   4 3 2   9 9 9
```

[**`task_4.7.py`**](task_4.7.py)

----

#### **Задание 4.8** ####

Реализовать программу, которая сжимает последовательность символов. На вход
подаётся последовательность вида `aaabbccccdaa`. Необходимо вывести строку,
состоящую из символов и количества повторений этого символа. Вывод должен
выглядеть как `a3b2c4d1a2`.

```python
def compress_str(ini_str):
    compressed_str = ''
    symbol = ini_str[0]
    counter = 1
    for num in range(1, len(ini_str)):
        if ini_str[num] == symbol:
            counter += 1
        else:
            compressed_str += (symbol + str(counter))
            symbol = ini_str[num]
            counter = 1
    compressed_str += (symbol + str(counter))
    return compressed_str
```

----

#### **Задание 5.4** ####

Написать функцию `distance_between_dots()`. Функция должна получать на вход
координаты двух точек (в виде четырёх чисел) и возвращать расстояние между ними.
Чтобы посчитать расстояние между точками, нужно воспользоваться формулой:    
`distance = sqrt((x1-x2)**2 + (y1-y2)**2)`    
Не забыть проверить значения полученных аргументов!

```python
def distance_between_dots(x_1, y_1, x_2, y_2):
    try:
        x1 = float(x_1)
        x2 = float(x_2)
        y1 = float(y_1)
        y2 = float(y_2)
    except:
        print('Something wrong!')
    else:
        return ((x1-x2)**2 + (y1-y2)**2) ** 0.5
```

----

#### **Задание 5.5** ####

Написать функцию, которая вычисляет среднее арифметическое значений списка.    
***Примечание***    
Среднее арифметическое считается как сумма всех чисел, делённая на их
количество.    
Не забыть проверить значение полученного аргумента!

```python
def arithmean(in_list):
    try:
        for digit in in_list:
            probe = float(digit)
    except:
        print('Something wrong!')
    else:
        return sum(in_list) / len(in_list)
```

----

#### **Задание 5.6** ####

Переписать функцию из предыдущей задачи (5.5) в виде lambda-функции.

```python
arithmean = lambda list_: sum(list_) / len(list_)
```

----

#### **Задание 5.7** ####

Написать функцию, которая принимает на вход строку и подсчитывает в ней
количество слов начинающихся на каждую букву алфавита. Возвращать функция должна
словарь следующего вида:    
`{'a': 10, 'b': 3, 'c': 0, ...}`    
Для задания словаря использовать строку с алфавитом:    
`alphabet_str = 'abcdefghijklmnopqrstuvwxyz'`    
Словарь с буквами создать с помощью генератора. Не забыть, что слова в
предложении могут начинаться с большой буквы.

[**`task_5.7.py`**](task_5.7.py)

```python
print(wordcount(sample1))
# {'a': 7, 'b': 8, 'c': 5, 'd': 4, 'e': 2, 'f': 6, 'g': 1, 'h': 6, 'i': 6, 'j': 0, 'k': 2, 'l': 3, 'm': 4, 'n': 1, 'o': 5, 'p': 6, 'q': 0, 'r': 0, 's': 4, 't': 24, 'u': 0, 'v': 0, 'w': 1, 'x': 0, 'y': 5, 'z': 0}

print(wordcount(sample2))
# {'a': 4, 'b': 1, 'c': 1, 'd': 0, 'e': 1, 'f': 4, 'g': 3, 'h': 0, 'i': 3, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 6, 'o': 2, 'p': 0, 'q': 0, 'r': 5, 's': 1, 't': 11, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
```

----

#### **Задание 5.8** ####

Дан список пользователей:    
`users_list = ['admin', 'ivan', 'ivan_ivan']`    
Написать декоратор, который запрашивает имя пользователя и проверяет, есть ли
оно в списке пользователей. Если да, то мы можем выполнить следующую нашу
функцию:

```text
def get_data_from_database():
    print("Super secure data from database")
```

Если пользователя нет в списке, нужно вывести об этом сообщение и пропустить
выполнение функции `get_data_from_database()`.

```python
users_list = ['admin', 'ivan', 'ivan_ivan']

def auth_decor(func):
    def func_decor(*args, **kwargs):
        uname = input('Enter username: ')
        if uname in users_list:
            return func(*args, **kwargs)
        else:
            print('Wrong user!')
    return func_decor

@auth_decor
def get_data_from_database():
    print('Super secure data from database')


get_data_from_database()
```

----

#### **Задание на самопроверку** ####

Задана строка `S`, состоящая из малых латинских букв. Требуется узнать длину
наибольшей подстроки, в которой все буквы одинаковы.    
Например:
```text
    "" -> 0
    "a" -> 1
    "abbc" -> 2
    "adddaabaa" -> 3
```

```python
def get_longest_dup(string_in):
    if len(string_in) <= 1:
        return len(string_in)
    longest_dup = 1
    dup = 1
    for symbol in range(1, len(string_in)):
        if string_in[symbol] == string_in[symbol-1]:
            dup += 1
            if longest_dup < dup:
                longest_dup = dup
        else:
            dup = 1
    return longest_dup
```
