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
