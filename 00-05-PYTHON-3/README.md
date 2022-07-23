## Задачи из юнитов модуля PYTHON-3 (Условные операторы) ##

#### [**`task_1.4.py`**](https://github.com/stalkspectrum/sf-ds-course-all/blob/master/00-05-PYTHON-3/task_1.4.py) **Задание 1.4** ####

Записать выражение, которое вернет `True`, если указывается високосный год,
иначе `False`. Например, x = 2000 -> `True`; x = 1900 -> `False`; и так далее.

> 1. год, номер которого кратен 400, — високосный;
> 2. остальные годы, номер которых кратен 100, — невисокосные (например, годы
1700,.1800, 1900, 2100, 2200, 2300);
> 3. остальные годы, номер которых кратен 4, — високосные;
> 4. все остальные годы — невисокосные.

```python
def is_leap_year(y)
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    return False
```

#### [**`task_1.8.py`**](https://github.com/stalkspectrum/sf-ds-course-all/blob/master/00-05-PYTHON-3/task_1.8.py) **Задание 1.8** ####

Работа аналитика данных в больнице. Пусть переменные `diagnosis_1`,
`diagnosis_2` и `diagnosis_3` хранят информацию о наличии у пациента различных
хронических заболеваний ('yes' — да, 'no' — нет). С помощью операторов сравнения
и логических операторов проверить, что пациент страдает хотя бы одним из этих
заболеваний. Результатом должно стать булево число&nbsp;&mdash; `True` или
`False`. Занести этот результат в переменную result.

```python
diagnosis_1 = 'yes'
diagnosis_2 = 'no'
diagnosis_3 = 'no'
result = (diagnosis_1 == 'yes') or (diagnosis_2 == 'yes') or (diagnosis_3 = 'yes')
print(result)
```

#### **Задание 5.1** ####

Записать выражение, которое вернет `True`, когда каждое из чисел `a` и `b`
нечетное.

```python
def are_both_odd(a, b):
    return (a % 2 == 1) and (b % 2 != 0)
```

#### **Задание 5.3** ####

Есть заготовка функции&nbsp;&mdash; def get_wind_class(speed). Нужно написать
цикл, который возвращает из функции класс ветра в зависимости от его характера:

> 1. от 1 до 4 м/с - "weak [1]"
> 2. от 5-10 м/c - "moderate [2]"
> 3. от 11-18 м/c - "strong [3]"
> 4. от 19 м/c - "hurricane [4]"

В последней строке программа печатает результат (в зависимости от цифры в
скобках)

```python
def get_wind_class(speed):
    if speed <= 4:
        return 'weak [1]'
    elif speed <= 10:
        return 'moderate [2]'
    elif speed <= 18:
        return 'strong [3]'
    else:
        return 'hurricane [4]'

print(get_wind_class(3))
```

#### **Задание 5.4** ####

Дописать функцию check_user так, чтобы она по логину пользователя проверяла,
существует он или нет, после чего с помощью вложенного условия проверяла
правильность пароля этого пользователя. Функция должна возвращать только `True`
или `False`.

```python
user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
    }

def check_user(username, password):
    if user_database[username] == password:
        return True
    return Flase
```
