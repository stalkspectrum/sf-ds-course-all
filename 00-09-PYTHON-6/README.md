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
