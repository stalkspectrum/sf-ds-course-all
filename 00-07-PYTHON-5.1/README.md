## Задачи из юнитов модуля PYTHON-5.1 (Функции) ##

#### **Задание 2.3** ####

Написать функцию `get_total`, которая принимает на вход число единиц товара и
стоимость каждой единицы. Функция возвращает одно число&nbsp;&mdash; общую
стоимость данного числа товаров.

```python
def get_total(units, price):
    return units * price
```

----

#### **Задание 3.1** ####

Попробовать добавить в новую функцию `get_time` из примера выше проверку
скорости на равенство нулю. Если скорость равна нулю, вернуть `ValueError` с
сообщением `"Speed cannot be equal to 0!"`.

```python
def get_time(distance, speed):
    if speed == 0:
        raise ValueError('Speed cannot be equal to 0!')
    if distance < 0 or speed < 0:
        raise ValueError('Distance or speed cannot be below 0!')
    return distance / speed


try:
    print(get_time(100, 0))
except ValueError as e:
    print(e)
```

----

#### **Задание 3.5** ####

Дана функция `add_mark`:

```text
def add_mark(name, mark, journal=None):
    if journal is None:
        journal = {}
    journal[name] = mark
    return journal
```

Дополнить её код таким образом, чтобы возникала ошибка `ValueError` с текстом
`"Invalid Mark!"` при попытке поставить оценку не из списка: 2, 3, 4 или 5.

```python
def add_mark(name, mark, journal=None):
    if mark not in range(2, 6):
        raise ValueError('Invalid Mark!')
    if journal is None:
        journal = {}
    journal[name] = mark
    return journal


try:
    print(add_mark('Ivanov', 6))
except ValueError as e:
    print(e)
```

#### **Задание 5.1** ####

Написать функцию `mult`, которая считает произведение переданных в неё чисел
через запятую.
***Особое указание***    
Посчитать результат с использованием цикла `for`.

```python
def mult(*args):
    result = 1
    for num in args:
        result *= num
    return result
```

----

#### **Задание 6.3** ####

Написать lambda-функцию для расчёта гипотенузы прямоугольного треугольника: она
принимает на вход длины двух катетов и возвращает длину гипотенузы (третьей,
самой длинной стороны прямоугольного треугольника).

```python
hyp = lambda a, b: (a**2 + b**2) ** 0.5
print(hyp(3, 4))
```

----

#### **Задание 6.4** ####

Написать функцию `sort_sides`, которая сортирует переданный в неё список.
Входной список состоит из кортежей с парами чисел&nbsp;&mdash; длинами катетов
прямоугольных треугольников.    
Функция должна возвращать список, отсортированный по возрастанию длин гипотенуз
треугольников.    
***Примечание***    
Пригодится `lambda`-функция из предыдущего задания. При этом потребуется
заменить `lambda` от 2 аргументов на `lambda` от одного аргумента и обращаться к
элементам кортежа уже при вычислении гипотенузы.

```python
def sort_sides(l_in):
    l_in.sort(key=lambda cat: (cat[0]**2 + cat[1]**2) ** 0.5)
    return l_in
```

----

#### **Задание 7.9** ####

Написать функцию `get_less`, которая принимает на вход через запятую список,
состоящий из чисел, и ещё одно число.    
Функция должна вернуть первое найденное число из списка, которое меньше
переданного во втором аргументе. Если такого числа нет, необходимо вернуть
`None`.

```python
def get_less(list_in, number):
    for n in list_in:
        if n < number:
            return n
    return None
```

----

#### **Задание 7.10** ####

Написать функцию `split_date(date)`, которая принимает на вход строку, задающую
дату, в формате ддммгггг без разделителей. Функция должна вернуть кортеж из
чисел (int): день, месяц, год.    
***Примечание***    
Здесь пригодятся срезы строк.

```python
def split_date(date):
    return int(date[:2]), int(date[2:4]), int(date[-4:])
```

----

#### **Задание 7.11** ####

Написать функцию `is_prime(num)`, которая проверяет, является ли число простым.
Функция должна вернуть `True`, если число простое, иначе&nbsp;&mdash; `False`.    
***Примечание***    
Простым называют число, которое делится только на 1 или на само себя. Число 1
простым не является.

```python
def is_prime(number):
    if number == 1:
        return False
    divisor = 2
    while divisor <= number ** 0.5 + 1:
        if number % divisor == 0:
            return False
        divisor += 1
    return True
```

----

#### **Задание 7.12** ####

Написать функцию `between_min_max(...)`, которая принимает на вход числа через
запятую. Функция возвращает среднее арифметическое между максимальным и
минимальным значением этих чисел, то есть `(max + min)/2`.

```python
def between_min_max(*nums):
    return (max(nums) + min(nums)) / 2
```

----

#### **Задание 7.13** ####

Написать функцию `best_student(...)`, которая принимает на вход в виде
именованных аргументов фамилии студентов и их номера в рейтинге (нагляднее в
примере). Необходимо вернуть фамилию студента с минимальным номером по рейтингу.

```python
def best_student(**students):
    student = None
    rate = None
    for dude in students:
        if rate is None or rate > students[dude]:
            student = dude
            rate = students[dude]
    return student


print(best_student(Tom=12, Mike=3))
# Mike
print(best_student(Tom=12))
# Tom
print(best_student(Tom=12, Jerry=1, Jane=2))
# Jerry
```

----
