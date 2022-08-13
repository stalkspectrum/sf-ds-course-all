## Задачи из юнитов модуля PYTHON-9 () ##

#### **Задания 2.3-5** ####

```text
clients = [953421196, 953421161, 953421142, 953421186, 953421181, 953421144, 953421190, 953421184, 953421141, 953421193, 953421129, 953421158, 953421130, 953421177, 953421181, 953421136, 953421160, 953421184, 953421146, 953421175, 953421110, 953421139, 953421100, 953421116, 953421130, 953421179, 953421181, 953421136, 953421174, 953421167, 953421132, 953421195, 953421145, 953421108, 953421143, 953421133, 953421180, 953421149, 953421135, 953421195, 953421143, 953421131, 953421157, 953421189, 953421128, 953421132, 953421127, 953421151, 953421197, 953421160, 953421112, 953421155, 953421182, 953421168, 953421131, 953421156, 953421113, 953421102, 953421113, 953421192, 953421142, 953421105, 953421165, 953421175, 953421102, 953421195, 953421154, 953421165, 953421141, 953421166, 953421126, 953421143, 953421165, 953421150, 953421187, 953421129, 953421176, 953421169, 953421109, 953421177, 953421109, 953421150, 953421136, 953421140, 953421189, 953421198, 953421186, 953421159, 953421184, 953421182, 953421133, 953421103, 953421186, 953421132, 953421121, 953421107, 953421138, 953421190, 953421113, 953421161, 953421154, 953421161, 953421107, 953421113, 953421180, 953421191, 953421178, 953421116, 953421102, 953421167, 953421191, 953421187, 953421182, 953421118, 953421122, 953421157, 953421195, 953421141, 953421116, 953421176, 953421194, 953421163, 953421116, 953421197, 953421189, 953421177, 953421133, 953421138, 953421101, 953421116, 953421128, 953421104, 953421165, 953421113, 953421135, 953421150, 953421165, 953421154, 953421165, 953421161, 953421188, 953421177, 953421189, 953421128, 953421116, 953421177, 953421147, 953421152, 953421175, 953421151, 953421183, 953421195, 953421142, 953421132, 953421148, 953421112, 953421111, 953421121, 953421125, 953421171, 953421169, 953421127, 953421191, 953421194, 953421114, 953421112, 953421142, 953421144, 953421176, 953421120, 953421134, 953421183, 953421140, 953421144, 953421172, 953421189, 953421143, 953421188, 953421176, 953421142, 953421117, 953421140, 953421155, 953421158, 953421131, 953421187, 953421156, 953421120, 953421118, 953421184, 953421171, 953421186, 953421115, 953421101, 953421124, 953421151, 953421153, 953421141, 953421156, 953421144, 953421135, 953421109, 953421177, 953421144, 953421109, 953421148, 953421144, 953421111, 953421161, 953421133, 953421144, 953421118, 953421137, 953421182, 953421111, 953421178, 953421100, 953421160, 953421175, 953421171, 953421149, 953421156, 953421187, 953421198, 953421117, 953421100, 953421167, 953421118, 953421136, 953421101, 953421163, 953421133, 953421133, 953421136, 953421116, 953421141, 953421163, 953421152, 953421193, 953421197, 953421142, 953421172, 953421152, 953421190, 953421193, 953421102, 953421149, 953421117, 953421160, 953421161, 953421147, 953421170, 953421161, 953421147, 953421172, 953421174, 953421168, 953421121, 953421190, 953421162, 953421173, 953421110, 953421111, 953421154, 953421157, 953421161, 953421179, 953421191, 953421155, 953421139, 953421180, 953421189, 953421155, 953421109, 953421169, 953421174, 953421192, 953421104, 953421116, 953421112, 953421151, 953421169, 953421149, 953421176, 953421102, 953421136, 953421146, 953421152, 953421146, 953421152, 953421116, 953421108, 953421183, 953421128, 953421150, 953421158, 953421194, 953421136, 953421104, 953421139]
```

Из списка карт постоянных покупателей `clients` выбрать номер карты наиболее
частого клиента.

```python
from collections import Counter

cards = Counter(clients)
print(cards.most_common()[0])
# (953421116, 9)
print(cards.most_common()[0][0])
# 953421116
```

Сколько раз был в магазине покупатель с картой под номером `953421102`?

```python
print(cards[953421102])
# 5
```

Сколько уникальных номеров карт содержит список `clients`?

```python
print(len(list(cards)))
# 94
```

----

#### **Задание 3.2** ####

```text
temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5), ('2004', -8.2), ('2005', -1.6), ('2006', -5.9),('2007', -2.4), ('2008', -1.7), ('2009', -3.5), ('2010', -12.1), ('2011', -5.8), ('2012', -4.9), ('2013', -6.1), ('2014', -6.9), ('2015', -2.7), ('2016', -11.2), ('2017', -3.9), ('2018', -2.9), ('2019', -6.5), ('2020', 1.5)]
```

Дан список из кортежей `temps`. На первом месте в кортеже указан год в виде
строки, а на втором&nbsp;&mdash; средняя температура января в Петербурге в
указанном году.    
Необходимо напечатать словарь, в котором ключи&nbsp;&mdash; годы, а
значения&nbsp;&mdash; - показатели температуры. Ключи необходимо отсортировать в
порядке убывания соответствующих им температур.    
***Пример входа:***    
`temps =  [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]`    
***Пример вывода:***    
`OrderedDict([('2001', -2.5), ('2000', -4.4), ('2002', -4.4), ('2003', -9.5)])`

```python
from collections import OrderedDict

temps.sort(key=lambda x: x[1], reverse=True)
temp_dict = OrderedDict(temps)
print(temp_dict)
```

----

#### **Задания 3.5-7** ####

В списке `users` содержатся номера пользователей, которые ожидают ответа от
сервера (номера могут повторяться). Превратить этот список в очередь для
выполнения заданий.

```text
users = [6, 18, 4, 7, 8, 8, 5, 18, 12, 17, 13, 15, 6, 7, 9, 17, 18, 8, 4, 11, 10, 8, 2, 10, 6, 10, 10, 9]
```

```python
from collections import deque
queue = deque(users)
```

Извлечь элемент из начала очереди.

```python
print(queue.popleft())
```

В уже модифицированной очереди переместить пять элементов из начала очереди в её
конец. Извлечь последний элемент из очереди.

```python
queue.rotate(-5)
last_task = queue.pop()
print(last_task)
```

Сколько задач с тем номером, что был извлечён в предыдущем задании, осталось в
модифицированной очереди?

```python
print(queue.count(last_task))
```

----

#### **Задание 4.3** ####

Написать функцию `brackets(line)`, которая определяет, является ли
последовательность из круглых скобок правильной. Правильной скобочной
последовательностью называется такая последовательность скобок, в которой для
каждой открывающей скобки есть последующая соответствующая ей закрывающая
скобка. Пустую строку считать правильной последовательностью.    
Для решения этой задачи потребуется использовать стек. Посимвольно перебрать
строку. Если встретилась открывающаяся скобка, положить её в стек. Если
встретилась закрывающаяся скобка, извлечь скобку из стека.

1. Если стек пустой, то есть извлечь скобку нельзя, последовательность
неправильная.
2. Если строка закончилась и стек стал пустым, последовательность правильная.
3. Если в стеке остались скобки, последовательность неправильная.

```python
from collections import deque

def brackets(line):
    queue = deque()
    for char in line:
        if char == '(':
            queue.append('(')
        if char == ')':
            if queue.count('(') > 0:
                queue.remove('(')
            else:
                return False
    if len(queue) == 0:
        return True
    return False
```

----

#### **Задания 4.4-8** ####

В переменных `center`, `south` и `north` хранятся списки из перечней купленных
позиций в трёх торговых точках, расположенных в разных районах города.

```text
north = [['Milk', 'Milk', 'Beer'], ['Chocolate', 'Bread', 'Chips'], ['Cola', 'Cola', 'Yoghurt', 'Soap', 'Beer', 'Chips', 'Milk'], ['Soap', 'Soap', 'Cola', 'Cola', 'Chips'], ['Milk', 'Beer', 'Meat', 'Ketchup', 'Cola', 'Cola', 'Chips', 'Chips', 'Cola', 'Cola'], ['Beer', 'Bread', 'Bread', 'Beer', 'Beer', 'Beer', 'Bread', 'Cheese'], ['Yoghurt', 'Beer', 'Chips', 'Milk', 'Soap', 'Cola', 'Cola', 'Cola', 'Beer', 'Cola', 'Cola', 'Cola', 'Beer', 'Ketchup', 'Beer', 'Beer', 'Beer', 'Soap'], ['Milk', 'Cola', 'Cola', 'Beer', 'Beer', 'Bread', 'Bread', 'Soap', 'Cola', 'Cola', 'Beer', 'Meat', 'Bread', 'Chips'], ['Beer', 'Beer', 'Beer', 'Chips', 'Milk', 'Cola', 'Chocolate', 'Beer', 'Chocolate', 'Beer', 'Beer', 'Cola', 'Meat', 'Yoghurt', 'Beer'], ['Bread'], ['Chocolate', 'Beer', 'Meat', 'Yoghurt'], ['Cola', 'Beer', 'Beer', 'Beer', 'Chocolate', 'Beer', 'Soap', 'Beer', 'Chips', 'Soap', 'Chocolate', 'Bread', 'Chips', 'Cola', 'Bread', 'Beer', 'Cola', 'Bread'], ['Chips', 'Cola', 'Beer', 'Chips', 'Cola', 'Cola', 'Beer', 'Soap', 'Yoghurt', 'Yoghurt', 'Cola', 'Bread', 'Beer', 'Chocolate', 'Chips', 'Bread', 'Beer', 'Bread'], ['Cola', 'Chocolate'], ['Chocolate', 'Cola', 'Meat', 'Cola', 'Ketchup', 'Cola', 'Chocolate', 'Bread', 'Chocolate', 'Chocolate', 'Meat'], ['Bread', 'Milk', 'Chips', 'Ketchup', 'Cola', 'Cola', 'Cola', 'Beer', 'Beer', 'Soap', 'Beer', 'Cola'], ['Yoghurt', 'Milk', 'Soap', 'Bread', 'Cola', 'Cola', 'Milk', 'Bread', 'Chips', 'Cheese', 'Milk', 'Yoghurt', 'Bread', 'Yoghurt'], ['Cola', 'Ketchup'], ['Cola', 'Yoghurt', 'Bread', 'Cola', 'Cola', 'Chips', 'Yoghurt', 'Milk', 'Beer', 'Chips', 'Bread', 'Beer', 'Beer', 'Cola', 'Bread', 'Beer', 'Beer', 'Cheese'], ['Beer', 'Cheese', 'Ketchup', 'Beer'], ['Beer', 'Beer', 'Beer'], ['Soap', 'Beer', 'Beer', 'Chocolate', 'Cola', 'Chocolate', 'Bread', 'Beer', 'Milk', 'Bread', 'Beer', 'Chocolate', 'Bread', 'Cola', 'Cola', 'Cheese', 'Beer', 'Cola', 'Soap', 'Yoghurt'], ['Beer', 'Chocolate'], ['Cola', 'Beer'], ['Yoghurt', 'Beer', 'Yoghurt', 'Yoghurt', 'Chips', 'Meat', 'Beer', 'Chocolate', 'Cola', 'Cola', 'Chips', 'Bread'], ['Cola', 'Cola', 'Cola', 'Cola', 'Cola', 'Bread', 'Chips', 'Soap', 'Cola', 'Chocolate', 'Beer', 'Beer'], ['Beer', 'Cola', 'Cola', 'Bread', 'Soap', 'Beer', 'Meat', 'Beer', 'Beer', 'Beer', 'Cola', 'Chips', 'Beer', 'Cola', 'Cola', 'Bread', 'Cheese', 'Beer'], ['Cola', 'Cola', 'Ketchup', 'Beer', 'Yoghurt', 'Bread'], ['Chips', 'Yoghurt', 'Cola', 'Cola', 'Cola', 'Chocolate', 'Chips', 'Bread', 'Chocolate', 'Yoghurt', 'Chocolate', 'Milk', 'Bread', 'Bread', 'Soap', 'Milk', 'Soap', 'Cola', 'Bread', 'Beer'], ['Beer', 'Beer', 'Ketchup', 'Cola', 'Beer', 'Bread', 'Beer', 'Cola', 'Beer', 'Chocolate'], ['Beer', 'Chocolate', 'Cola', 'Beer', 'Yoghurt', 'Milk', 'Bread', 'Cheese', 'Yoghurt', 'Beer', 'Cola', 'Yoghurt', 'Cola', 'Soap', 'Beer', 'Bread', 'Meat', 'Bread', 'Cola'], ['Beer', 'Cola', 'Chips', 'Cola'], ['Cola', 'Cola', 'Beer', 'Cheese'], ['Bread', 'Soap', 'Ketchup', 'Chocolate', 'Beer', 'Cola', 'Chocolate', 'Cola', 'Cola', 'Yoghurt', 'Beer', 'Bread', 'Cola', 'Ketchup', 'Beer'], ['Bread'], ['Bread', 'Beer', 'Yoghurt', 'Yoghurt', 'Bread', 'Milk', 'Soap', 'Meat', 'Bread', 'Beer', 'Cola', 'Milk', 'Milk', 'Bread', 'Beer', 'Cola', 'Ketchup', 'Cola'], ['Bread', 'Beer', 'Bread', 'Yoghurt', 'Beer', 'Bread', 'Cola', 'Cola', 'Cola', 'Beer', 'Bread', 'Milk', 'Chips', 'Cola', 'Beer', 'Bread', 'Soap', 'Bread', 'Yoghurt', 'Bread'], ['Yoghurt', 'Beer', 'Cola', 'Beer', 'Beer', 'Beer'], ['Chips', 'Chocolate', 'Soap', 'Chocolate', 'Cola', 'Bread', 'Beer', 'Cola', 'Beer', 'Ketchup', 'Chocolate', 'Ketchup', 'Ketchup', 'Cheese', 'Chips', 'Beer', 'Chips', 'Chocolate'], ['Bread', 'Cola', 'Cola', 'Beer', 'Bread', 'Bread', 'Beer', 'Chocolate', 'Bread', 'Cola', 'Milk', 'Chips', 'Meat', 'Beer', 'Beer', 'Soap', 'Bread'], ['Beer', 'Beer', 'Bread', 'Chips', 'Beer', 'Bread', 'Bread', 'Chips', 'Beer'], ['Yoghurt', 'Bread', 'Cola', 'Bread', 'Cola', 'Bread', 'Meat', 'Cola', 'Bread', 'Beer', 'Soap', 'Chips'], ['Bread', 'Beer'], ['Milk', 'Beer', 'Meat', 'Cola', 'Beer', 'Cola', 'Cola'], ['Beer', 'Chips', 'Yoghurt', 'Beer', 'Cola', 'Beer', 'Cola', 'Cola', 'Soap', 'Cola'], ['Bread', 'Cola', 'Cola', 'Meat'], ['Cola', 'Chocolate', 'Meat', 'Beer', 'Cola', 'Bread', 'Chips', 'Beer', 'Chips', 'Chips', 'Cola'], ['Bread', 'Cola', 'Cola', 'Cola', 'Beer', 'Cola', 'Yoghurt', 'Beer', 'Chips', 'Cola', 'Chocolate', 'Chips', 'Cola', 'Cola', 'Cola', 'Cola', 'Bread', 'Cola'], ['Cola', 'Soap', 'Cola'], ['Soap', 'Chips', 'Cola', 'Beer', 'Bread', 'Soap', 'Cheese', 'Bread', 'Beer', 'Chocolate']]
center = [['Meat', 'Beer', 'Soap', 'Beer', 'Cheese', 'Cola', 'Milk', 'Soap', 'Cola', 'Meat', 'Bread', 'Chocolate', 'Chips'], ['Soap', 'Beer', 'Chips', 'Bread', 'Beer', 'Beer', 'Beer', 'Cheese', 'Cheese', 'Beer', 'Chips', 'Chocolate', 'Chips', 'Cheese', 'Bread', 'Cola', 'Cola', 'Beer'], ['Cola', 'Soap', 'Bread', 'Milk', 'Beer', 'Meat', 'Bread', 'Bread'], ['Ketchup', 'Beer', 'Ketchup', 'Chocolate', 'Milk', 'Milk', 'Bread', 'Beer'], ['Beer', 'Beer', 'Meat', 'Ketchup', 'Soap', 'Bread', 'Cola', 'Beer'], ['Meat', 'Bread', 'Milk', 'Cheese', 'Soap', 'Beer', 'Milk', 'Cheese', 'Cola', 'Beer', 'Chips', 'Bread', 'Ketchup', 'Chocolate', 'Bread', 'Milk'], ['Yoghurt'], ['Beer', 'Milk', 'Chips', 'Soap', 'Chips', 'Milk', 'Beer', 'Chips', 'Bread', 'Meat', 'Milk'], ['Yoghurt', 'Beer', 'Cola', 'Cola', 'Beer', 'Soap', 'Cheese', 'Soap', 'Bread', 'Cola', 'Yoghurt', 'Ketchup', 'Beer', 'Milk'], ['Milk', 'Cola', 'Bread', 'Cola', 'Bread', 'Beer', 'Beer', 'Beer'], ['Yoghurt', 'Cola'], ['Bread', 'Yoghurt', 'Chips', 'Ketchup', 'Meat', 'Bread', 'Beer', 'Yoghurt', 'Cola', 'Cola'], ['Chips', 'Chocolate', 'Chips', 'Meat', 'Bread', 'Cheese', 'Bread', 'Yoghurt'], ['Ketchup', 'Soap', 'Chocolate', 'Bread'], ['Chips', 'Beer', 'Chips', 'Cola', 'Cheese', 'Soap', 'Ketchup', 'Meat', 'Cola', 'Chips', 'Beer', 'Chocolate', 'Beer', 'Milk', 'Bread', 'Ketchup', 'Chips', 'Cheese', 'Ketchup'], ['Beer', 'Milk', 'Soap', 'Chips', 'Soap', 'Bread', 'Bread', 'Milk', 'Beer'], ['Cola', 'Chips', 'Meat', 'Cola', 'Beer', 'Chocolate', 'Bread', 'Bread', 'Chips', 'Soap', 'Chocolate', 'Chips', 'Beer'], ['Meat', 'Cola', 'Chips', 'Bread', 'Chips', 'Chocolate', 'Bread', 'Meat', 'Bread', 'Yoghurt', 'Cheese', 'Bread', 'Chips', 'Cola'], ['Chips', 'Cheese', 'Bread', 'Beer', 'Bread', 'Chips', 'Chocolate', 'Bread', 'Cola', 'Cola', 'Chocolate', 'Chocolate', 'Bread', 'Meat', 'Chips'], ['Bread', 'Milk', 'Bread', 'Cheese', 'Bread', 'Cheese', 'Ketchup', 'Beer', 'Cheese', 'Cola', 'Milk', 'Milk', 'Bread', 'Beer', 'Bread', 'Chips'], ['Yoghurt'], ['Bread', 'Bread', 'Chips', 'Cheese', 'Bread', 'Beer', 'Cola', 'Ketchup', 'Bread', 'Chips', 'Chocolate', 'Meat', 'Milk', 'Beer', 'Milk', 'Cheese', 'Bread', 'Meat', 'Bread', 'Cola'], ['Bread', 'Meat', 'Meat', 'Milk', 'Chips', 'Soap', 'Yoghurt', 'Chips', 'Beer', 'Yoghurt'], ['Bread', 'Soap', 'Bread', 'Cola', 'Bread'], ['Cola', 'Bread', 'Meat', 'Cola', 'Meat', 'Chocolate', 'Chips', 'Meat', 'Chips'], ['Chips', 'Cheese', 'Cheese', 'Meat'], ['Chips', 'Meat', 'Soap', 'Cheese', 'Bread', 'Cola', 'Bread', 'Beer', 'Meat', 'Cola', 'Bread', 'Cola', 'Ketchup', 'Bread'], ['Chips', 'Cheese', 'Milk', 'Meat', 'Milk', 'Beer', 'Chocolate', 'Ketchup', 'Cola', 'Cheese', 'Beer'], ['Beer', 'Ketchup', 'Yoghurt', 'Ketchup', 'Chocolate', 'Bread', 'Beer', 'Ketchup', 'Chocolate', 'Cola', 'Chocolate', 'Ketchup', 'Cola', 'Meat', 'Chips', 'Soap', 'Meat'], ['Meat', 'Milk'], ['Cola', 'Beer', 'Yoghurt', 'Beer', 'Bread', 'Cola'], ['Chips', 'Meat', 'Cheese', 'Ketchup', 'Chips', 'Bread', 'Bread', 'Chips', 'Chips', 'Bread', 'Milk', 'Ketchup', 'Cola', 'Cola', 'Beer'], ['Beer', 'Bread', 'Cheese', 'Bread', 'Cola', 'Cheese', 'Cheese', 'Beer', 'Milk', 'Bread', 'Chocolate', 'Cheese', 'Beer', 'Bread', 'Beer', 'Cola', 'Yoghurt', 'Beer', 'Beer', 'Chips'], ['Bread', 'Chips', 'Bread', 'Cola', 'Chips', 'Chocolate', 'Cheese', 'Beer', 'Chips', 'Milk', 'Milk', 'Beer', 'Cola', 'Meat', 'Cola', 'Bread', 'Cola', 'Chocolate', 'Chocolate', 'Cola'], ['Soap', 'Yoghurt', 'Chips', 'Beer', 'Chips', 'Milk', 'Cheese', 'Meat', 'Beer', 'Bread', 'Ketchup', 'Bread', 'Bread', 'Cheese', 'Milk', 'Beer', 'Beer', 'Soap', 'Bread'], ['Cola', 'Bread', 'Cheese', 'Ketchup', 'Beer', 'Chips', 'Meat', 'Chocolate', 'Chips', 'Cola', 'Beer', 'Beer', 'Cola'], ['Ketchup', 'Beer', 'Chocolate', 'Bread', 'Yoghurt', 'Beer', 'Cheese'], ['Bread', 'Chocolate', 'Bread', 'Milk'], ['Meat', 'Yoghurt', 'Bread', 'Yoghurt', 'Cola', 'Ketchup'], ['Ketchup', 'Bread', 'Bread', 'Chocolate', 'Chocolate', 'Chocolate', 'Bread', 'Bread', 'Beer', 'Chocolate', 'Bread', 'Milk'], ['Bread', 'Cheese', 'Soap', 'Soap', 'Chips', 'Chips'], ['Ketchup', 'Chocolate', 'Chips', 'Milk', 'Soap', 'Soap', 'Ketchup', 'Bread', 'Ketchup', 'Cola', 'Cheese', 'Beer', 'Ketchup', 'Bread'], ['Bread', 'Milk', 'Beer', 'Yoghurt', 'Meat', 'Ketchup', 'Meat', 'Meat', 'Bread', 'Milk', 'Cheese', 'Beer', 'Yoghurt', 'Milk', 'Bread', 'Cola'], ['Chips', 'Cola', 'Milk', 'Chocolate', 'Beer', 'Beer', 'Chips', 'Bread', 'Beer', 'Beer', 'Bread', 'Beer', 'Ketchup', 'Milk', 'Yoghurt', 'Ketchup', 'Cola', 'Ketchup', 'Chips', 'Meat'], ['Beer', 'Bread', 'Soap', 'Cheese', 'Meat', 'Soap'], ['Beer', 'Meat', 'Beer', 'Yoghurt', 'Soap', 'Chips', 'Meat', 'Cheese', 'Milk', 'Bread', 'Meat', 'Beer', 'Milk'], ['Chips', 'Meat', 'Bread'], ['Chocolate', 'Soap', 'Bread', 'Chips', 'Chips', 'Yoghurt', 'Chips', 'Cola', 'Cola', 'Cola', 'Beer', 'Milk', 'Milk', 'Bread', 'Bread', 'Meat'], ['Meat', 'Chocolate', 'Chips', 'Chips', 'Yoghurt', 'Yoghurt', 'Beer', 'Cola', 'Cheese', 'Milk', 'Beer'], ['Meat', 'Chocolate', 'Yoghurt', 'Cola', 'Cheese', 'Meat', 'Bread', 'Beer', 'Meat', 'Beer', 'Yoghurt', 'Cola', 'Bread']]
south = [['Cola', 'Meat', 'Cheese', 'Yoghurt', 'Beer', 'Milk', 'Milk', 'Meat', 'Cola', 'Cola', 'Cheese', 'Beer', 'Yoghurt', 'Beer', 'Bread', 'Bread', 'Milk', 'Cheese', 'Chocolate'], ['Soap', 'Milk', 'Cola'], ['Milk', 'Bread', 'Yoghurt', 'Meat', 'Meat'], ['Bread', 'Milk', 'Beer'], ['Beer'], ['Chocolate', 'Meat', 'Chocolate', 'Cola', 'Cola', 'Cola', 'Cola', 'Yoghurt', 'Bread', 'Meat', 'Soap', 'Soap', 'Milk', 'Milk', 'Cola'], ['Beer', 'Beer', 'Meat', 'Chips', 'Bread', 'Bread', 'Bread', 'Bread', 'Milk', 'Cola', 'Chocolate', 'Bread', 'Beer', 'Chips', 'Bread', 'Bread', 'Yoghurt'], ['Chips', 'Milk', 'Soap'], ['Meat', 'Beer', 'Milk', 'Chocolate', 'Bread', 'Yoghurt'], ['Chips', 'Meat', 'Chocolate', 'Bread', 'Cola', 'Cola', 'Chocolate', 'Meat', 'Yoghurt', 'Milk'], ['Bread', 'Soap', 'Bread', 'Meat', 'Beer', 'Yoghurt', 'Milk', 'Cola', 'Bread', 'Ketchup'], ['Meat', 'Milk'], ['Meat', 'Beer', 'Yoghurt'], ['Cola', 'Bread', 'Cola', 'Chocolate', 'Chips', 'Meat', 'Cheese'], ['Milk', 'Milk', 'Cheese', 'Meat'], ['Chips', 'Yoghurt', 'Cheese', 'Soap', 'Ketchup', 'Cheese', 'Soap', 'Beer', 'Ketchup', 'Ketchup', 'Milk', 'Bread', 'Bread', 'Beer'], ['Meat'], ['Ketchup', 'Bread', 'Beer', 'Milk', 'Bread', 'Meat', 'Ketchup', 'Cheese'], ['Meat', 'Chips', 'Bread', 'Meat', 'Milk', 'Soap', 'Chocolate', 'Meat', 'Chocolate', 'Chocolate', 'Bread', 'Cheese', 'Soap', 'Cola', 'Yoghurt'], ['Cheese', 'Milk', 'Bread', 'Milk', 'Chips', 'Chips', 'Meat', 'Beer', 'Chocolate', 'Chocolate'], ['Ketchup', 'Beer', 'Cheese', 'Cola'], ['Chocolate', 'Cheese', 'Bread'], ['Milk', 'Yoghurt', 'Ketchup', 'Beer', 'Meat', 'Chips', 'Yoghurt', 'Meat', 'Bread', 'Chips'], ['Yoghurt', 'Milk', 'Ketchup', 'Yoghurt', 'Beer', 'Cheese', 'Bread', 'Bread', 'Ketchup', 'Bread', 'Bread', 'Yoghurt', 'Meat'], ['Soap', 'Meat', 'Bread', 'Beer', 'Milk'], ['Beer', 'Cola', 'Beer', 'Meat', 'Meat', 'Cheese', 'Meat', 'Chocolate', 'Bread', 'Ketchup', 'Milk', 'Soap'], ['Cheese', 'Chocolate', 'Milk', 'Chocolate', 'Cola', 'Bread', 'Chips', 'Cheese', 'Soap', 'Ketchup', 'Cheese', 'Chips', 'Cheese', 'Cola', 'Chocolate', 'Beer'], ['Bread', 'Bread', 'Cola', 'Ketchup', 'Cola', 'Bread', 'Meat', 'Yoghurt', 'Milk', 'Beer', 'Beer', 'Cheese', 'Meat', 'Bread', 'Cheese', 'Meat', 'Chocolate'], ['Chocolate', 'Soap', 'Chips', 'Beer', 'Bread', 'Yoghurt', 'Chips', 'Chocolate', 'Beer', 'Cheese', 'Cola', 'Milk', 'Chips', 'Milk', 'Ketchup', 'Cola', 'Meat', 'Beer', 'Cheese', 'Yoghurt'], ['Soap'], ['Meat', 'Beer', 'Milk', 'Bread', 'Beer', 'Cheese', 'Chocolate', 'Beer', 'Beer', 'Milk', 'Beer', 'Bread', 'Meat', 'Beer', 'Chocolate', 'Beer', 'Soap', 'Chips', 'Cola'], ['Cola', 'Beer', 'Meat', 'Chips', 'Soap', 'Cola', 'Bread', 'Cola', 'Bread', 'Chips', 'Ketchup', 'Ketchup', 'Beer', 'Ketchup', 'Cola', 'Milk', 'Cheese'], ['Cheese', 'Milk', 'Chips', 'Bread', 'Yoghurt', 'Soap', 'Beer', 'Chips', 'Ketchup', 'Chips', 'Beer', 'Yoghurt', 'Cola', 'Cheese', 'Chocolate', 'Beer'], ['Meat', 'Bread', 'Meat', 'Bread'], ['Cola', 'Beer', 'Yoghurt'], ['Beer', 'Bread', 'Beer', 'Meat', 'Bread', 'Milk', 'Soap', 'Milk', 'Chocolate', 'Meat', 'Meat', 'Meat', 'Chips', 'Chocolate', 'Meat'], ['Beer', 'Cola', 'Chocolate', 'Bread', 'Cheese', 'Cheese'], ['Milk', 'Chips', 'Cola', 'Milk', 'Bread', 'Bread', 'Beer', 'Milk', 'Cola', 'Chocolate', 'Chocolate', 'Meat', 'Cola', 'Cola', 'Beer', 'Cola', 'Chocolate', 'Bread', 'Bread', 'Cola'], ['Chocolate', 'Chocolate', 'Beer', 'Beer', 'Bread', 'Yoghurt', 'Meat', 'Cola', 'Yoghurt'], ['Ketchup', 'Cola', 'Ketchup', 'Yoghurt', 'Chips', 'Soap', 'Soap', 'Chocolate', 'Chocolate', 'Bread', 'Beer', 'Meat'], ['Bread', 'Meat', 'Soap', 'Cola', 'Bread', 'Cola', 'Yoghurt', 'Meat', 'Bread', 'Cola', 'Cola', 'Ketchup', 'Beer', 'Bread', 'Milk', 'Yoghurt', 'Meat'], ['Chocolate', 'Yoghurt', 'Bread'], ['Meat', 'Bread', 'Bread', 'Bread'], ['Beer', 'Milk', 'Cola', 'Ketchup', 'Cola', 'Cheese', 'Meat', 'Chocolate'], ['Soap', 'Beer', 'Chocolate', 'Chocolate', 'Cola', 'Cola', 'Yoghurt', 'Ketchup', 'Milk'], ['Meat', 'Yoghurt', 'Bread', 'Ketchup', 'Ketchup', 'Milk', 'Meat'], ['Ketchup', 'Soap', 'Chips', 'Ketchup', 'Bread', 'Chocolate', 'Milk', 'Bread', 'Bread', 'Ketchup', 'Cola', 'Meat', 'Milk', 'Bread', 'Cola'], ['Meat', 'Beer', 'Yoghurt', 'Chips', 'Beer', 'Meat', 'Cola', 'Beer', 'Meat', 'Ketchup', 'Milk', 'Cola', 'Yoghurt', 'Beer', 'Meat', 'Bread', 'Bread'], ['Meat', 'Soap', 'Cheese', 'Ketchup', 'Cola', 'Cola', 'Bread', 'Chips', 'Meat', 'Cola', 'Bread', 'Beer', 'Beer', 'Beer'], ['Meat', 'Yoghurt', 'Bread', 'Milk', 'Beer', 'Beer']]
```

Надо вначале избавиться от излишней вложенности: в каждой переменной (`center`,
`south`, `north`) должен храниться объединённый список купленных товаров без
разбиения по чекам.    
***Пример:***    
`[['Milk', 'Bread'], ['Meat']] -> ['Milk', 'Bread', 'Meat']`    
После этого определить, в каком магазине было куплено больше всего товаров.

```python
def flat_list(list_in):
    flatlist = []
    for sublist in list_in:
        flatlist.extend(sublist)
    return flatlist


print(f'NORTH total = {len(flat_list(north))}')
print(f'CENTER total = {len(flat_list(center))}')
print(f'SOUTH total = {len(flat_list(south))}')
```

Получить объекты-счётчики (Counter) из каждого полученного в предыдущем задании
списка покупок и сохранить их в отдельные переменные (они пригодятся для
следующих задач).    
Сколько раз покупали самый редкий товар в магазине `north`?

```python
from collections import Counter

north_cnt = Counter(flat_list(north))
center_cnt = Counter(flat_list(center))
south_cnt = Counter(flat_list(south))

print(north_cnt.most_common()[-1])
```

Выбрать товары, который в магазине `center` покупали чаще, чем в магазине
`north`.

```python
# Посмотреть глазами
print(center_cnt - north_cnt)
```

Есть ли такой товар, который в одном из магазинов покупали чаще, чем в двух
других вместе взятых? Если да, выбрать магазин с настолько популярным товаром.

```python
# Посмотреть глазами
print(north_cnt.most_common())
print(center_cnt.most_common())
print(south_cnt.most_common())

for good in list(north_cnt):
    print(f'{good} in: north={north_cnt[good]}',
                    f'center={center_cnt[good]}',
                    f'south={south_cnt[good]}',
                    sep=' ')
```

Определить суммарное число продаж каждого товара во всех магазинах, сложив все
объекты-счётчики. Сколько раз был куплен второй по популярности товар?

```python
# Посмотреть глазами
print((north_cnt + center_cnt + south_cnt).most_common()[1])
```

----

#### **Задание 4.9** ####

Дан список кортежей `ratings` с рейтингами кафе. Кортеж состоит из названия и
рейтинга кафе.

```text
ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8), ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1), ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]
```

Необходимо отсортировать список кортежей по убыванию рейтинга в `ratings`. Если
рейтинги совпадают, то отсортировать кафе дополнительно по названию в алфавитном
порядке.    
Получить словарь `cafes` с упорядоченными ключами из отсортированного списка,
где ключи&nbsp;&mdash; названия кафе, а значения&nbsp;&mdash; их рейтинг.

```python
from collections import OrderedDict

ratings.sort()
ratings.sort(key=lambda x: x[1], reverse=True)
cafes = OrderedDict(ratings)

print(cafes)
# OrderedDict([('WokAndRice', 4.9), ('WokToWork', 4.9), ('General Foods', 4.8), ('New Age', 4.6), ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1), ('Nice Cakes', 3.9), ('Old Gold', 3.3), ('Old Wine Cellar', 3.3), ('Old York', 3.3)])
```

----

#### **Задание 4.10** ####

Написать функцию `task_manager(tasks)`, которая принимает список задач для
нескольких серверов. Каждый элемент списка состоит из кортежа (&lt;номер
задачи&gt;, &lt;название сервера&gt;, &lt;высокий приоритет задачи&gt;).    
Функция должна создавать словарь и заполнять его задачами по следующему
принципу: название сервера&nbsp;&mdash; ключ, по которому хранится очередь задач
для конкретного сервера.    
Если поступает задача без высокого приоритета (последний элемент кортежа&nbsp;&mdash;
`False`), добавить номер задачи в конец очереди. Если приоритет высокий,
добавить номер в начало.    
Для словаря использовать `defaultdict`, для очереди&nbsp;&mdash; `deque`.
Функция возвращает полученный словарь с задачами.    
***Пример***    

```text
tasks = [(36871, 'office', False),
         (40690, 'office', False),
         (35364, 'voltage', False),
         (41667, 'voltage', True),
         (33850, 'office', False)]
```

```python
from collections import defaultdict, deque

def task_manager(tasks):
    task_dict = defaultdict(deque)
    for task in tasks:
        ident, server, urgent = task
        if urgent:
            task_dict[server].appendleft(ident)
        else:
            task_dict[server].append(ident)
    return task_dicr


print(task_manager(tasks))
# defaultdict(, {'voltage': deque([41667, 35364]), 'office': deque([36871, 40690, 33850])})
```

----

#### **Задания 6.8-12** ####

```text
import mystery
print(mystery)
[[[      inf       inf       inf   6112.         inf       inf       inf]
  [      inf       inf       inf -51040.         inf       inf       inf]
  [ -5432.         inf       inf       inf       inf       inf       inf]
  [      inf       inf       inf       inf  26544.         inf      -inf]
  [      inf       inf       inf       inf       inf       inf       inf]]

 [[      inf -15896.         inf -34080.         inf       inf       inf]
  [      inf       inf       inf       inf       inf       inf       inf]
  [      inf       inf       inf       inf       inf       inf       inf]
  [      inf       inf       inf       inf       inf       inf       inf]
  [      inf       inf       inf       inf       inf       inf       inf]]

 [[-27664.         inf       inf       inf       inf       inf  64288.  ]
  [      inf       inf       inf       inf       inf       inf       inf]
  [      inf  56704.    44160.         inf       inf       inf  50912.  ]
  [      inf  30064.         inf       inf      -inf  60384.         inf]
  [      inf       inf -13000.         inf   3218.   -27904.        -inf]]

 [[      inf       inf    469.75       inf       inf       inf       inf]
  [  7808.         inf       inf -32832.         inf       inf       inf]
  [      inf       inf       inf       inf       inf       inf  43680.  ]
  [      inf       inf       inf       inf       inf       inf       inf]
  [-51392.         inf  12960.         inf       inf       inf       inf]]

 [[      inf       inf  44992.   -51136.         inf       inf       inf]
  [      inf       inf       inf       inf       inf       inf       inf]
  [-56480.         inf  48096.   -13608.         inf       inf -65472.  ]
  [      inf       inf       inf       inf       inf       inf       inf]
  [      inf       inf       inf       inf -18272.         inf       inf]]

 [[      inf       inf       inf       inf       inf       inf      -inf]
  [      inf       inf       inf       inf       inf  26176.         inf]
  [      inf       inf       inf       inf       inf       inf  24576.  ]
  [      inf       inf       inf       inf       inf       inf       inf]
  [      inf       inf       inf       inf      -inf -52640.         inf]]]
```

Узнать размерность массива `mystery`.

```python
print(mystery.ndim)
# 3
```

Какова максимальная протяжённость по одной из осей массива?

```python
print(mystery.shape)
# (6, 5, 7)
```

Узнать число элементов массива.

```python
print(mystery.size)
# 210
```

Какой тип данных у элементов массива?

```python
print(mystery.dtype)
# float16
```

Узнать вес всех элементов в массиве в байтах.

```python
print(mystery.itemsize * mystery.size)
# 420
```

----

#### **Задания 7.2** ####

```text
import mystery
print(mystery)
[[-13586  15203  28445 -27117  -1781 -17182 -18049]
 [ 25936 -30968  -1297  -4593   6451  15790   7181]
 [ 13348  28049  28655  -6012  21762  25397   8225]
 [ 13240   7994  32592  20149  13754  11795   -564]
 [-21725  -8681  30305  22260 -17918  12578  29943]
 [-16841 -25392 -17278  11740   5916    -47 -32037]]
```

В переменную `elem_5_3` сохранить элемент из 5 строки и 3 столбца:

```python
elem_5_3 = mystery[4, 2]
```

В переменную `last` сохранить элемент из последней строки последнего столбца:

```python
last = mystery[-1, -1]
```

В переменную `line_4` сохранить строку 4:

```python
line_4 = mystery[3, :]
```

В переменную `col_2` сохранить предпоследний столбец:

```python
col_2 = mystery[:, -2]
```

Из строк 2-4 (включительно) получить столбцы 3-5 (включительно), результат
сохранить в переменную `part`:

```python
part = mystery[1:4, 2:5]
```

Сохранить в переменную `rev` последний столбец в обратном порядке:

```python
rev = mystery[::-1, -1]
```

Сохранить в переменную `trans` транспонированный массив:

```python
trans = mystery.transpose()
```

----

#### **Задания 7.4** ####

```text
import mystery
print(mystery)
[ 12279. -26024.  28745.     nan  31244.  -2365.  -6974.  -9212.     nan
 -17722.  16132.  25933.     nan -16431.  29810.]
```

Получить булевый массив с информацией о `np.nan` в массиве `mystery`.
`True`&nbsp;&mdash; значение пропущено, `False`&nbsp;&mdash; значение не
пропущено.

```python
nans_index = np.isnan(mystery)

print(nans_index)
# [False False False  True False False False False  True
#  False False False  True False False]
```

В переменную `n_nan` сохранить число пропущенных значений:

```python
n_nan = sum(np.isnan(mystery))

print(n_nan)
# 3
```

Заполнить пропущенные значения в массиве `mystery` нулями:

```python
mystery[np.isnan(mystery)] = 0

print(mystery)
# [ 12279. -26024.  28745.      0.  31244.  -2365.  -6974.  -9212.      0.
#  -17722.  16132.  25933.      0. -16431.  29810.]
```

Поменять тип данных в массиве `mystery` на `int32`:

```python
mystery = np.int32(mystery)

print(mystery)
# [ 12279 -26024  28745      0  31244  -2365  -6974  -9212      0 -17722
#   16132  25933      0 -16431  29810]
```

Отсортировать значения в массиве по возрастанию и сохранить результат в
переменную `array`:

```python
array = np.sort(mystery)

print(array)
# [-26024 -17722 -16431  -9212  -6974  -2365      0      0      0  12279
#   16132  25933  28745  29810  31244]
```

Сохранить в массив `table` двухмерный массив, полученный из массива `array`. В
нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть по
столбцам! Например:

```text
1, 2, 3, 4 -> 1    3
              2    4
```

```python
table = array.reshape((5, 3), order='F')

print(table)
# [[-26024  -2365  16132]
#  [-17722      0  25933]
#  [-16431      0  28745]
#  [ -9212      0  29810]
#  [ -6974  12279  31244]]
```

Сохранить в переменную `col` средний столбец из `table`:

```python
col = table[:, 1]

print(col)
# [-2365     0     0     0 12279]
```

----
