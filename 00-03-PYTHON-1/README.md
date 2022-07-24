## Задачи из юнитов модуля PYTHON-1 (Строки, форматированный вывод) ##

#### **Задание 8.6** ####

Написать небольшую программу, которая реализует ввод произвольного количества
чисел через пробел и выводит эти же самые числа построчно.

```python
num_str = input('Enter some numbers separated by space: ')
num_list = num_str.split()
print('\n'.join(num_list))
```

----

#### **Задание 8.8** ####

Написать программу, которая выводит на экран фразу в формате:

```text
Hello, <name>! Today is <dayofweek>. Have a nice day!
```

Пример: `Hello, John! Today is Friday. Have a nice day!`    
Информация о пользователе содержится в следующих переменных:

> `name` - имя пользователя    
> `dayofweek` - название дня недели    

Обязательное условие - задача должна быть решена с использованием метода format
(Codeboard не поддерживает f-строки, поэтому приходится использовать метод
format())

```python
name = 'John'
dayofweek = 'Friday'
print('Hello, {}! Today is {}. Have a nice day!'.format(name, dayofweek))
```
