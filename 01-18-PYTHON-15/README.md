## Задачи из юнитов модуля PYTHON-15 (Принципы ООП в Python) ##

#### **Задание 4.1** ####

Дописать определение класса `DepartmentReport`, который выводит отчёт по отделам
компании. У него должны быть определены:

- атрибут `revenues`&nbsp;&mdash; список, где мы храним значения выручки отделов;
- метод `add_revenue`, который добавляет выручку одного отдела;
- метод average_revenue, который возвращает среднюю выручку по всем отделам.

```python
class DepartmentReport():
    def add_revenue(self, amount):
        if not hasattr(self, revenues):
            self.revenues = []
        self.revenues.append(amount)

    def average_revenue(self):
        return sum(self.revenues) / len(self.revenues)


report = DepartmentReport_()
report.add_revenue(1_000_000)
report.add_revenue(400_000)
print(report.revenues)
# [1000000, 400000]
print(report.average_revenue())
# 700000.0
```

----

#### **Задание 4.2** ####

Улучшить класс `DepartmentReport`. Класс при инициализации должен принимать
переменную `company` и инициализировать её значением атрибут `company`, а также
инициализировать атрибут `revenues` пустым списком. Метод `average_revenue`
должен возвращать строку:    
`"Average department revenue for (company_name): (average_revenue)"`.

```python
class DepartmentReport():
    def __init__(self, company):
        self.revenues = []
        self.company = company

    def add_revenue(self, amount):
        self.revenues.append(amount)

    def average_revenue(self):
        average = round(sum(self.revenues) / len(self.revenues))
        return f'Average department revenue for {self.company}: {average}'


report = DepartmentReport("Danon")
report.add_revenue(1_000_000)
report.add_revenue(400_000)
print(report.average_revenue())
# Average department revenue for Danon: 700000
```

----

#### **Задание 5.1** ####

Определить класс для пользователей `User`:

- у него должны быть атрибуты `email`, `password` и `balance`, которые
устанавливаются при инициализации;
- у него должен быть метод `login`, который принимает емайл и пароль. Если они
совпадают с атрибутами объекта, он возвращает `True`, а иначе&nbsp;&mdash;
`False`;
- должен быть метод `update_balance(amount)`, который изменяет баланс счёта на
величину `amount`.

```python
class User():
    def __init__(self, email, password, balance):
        self.email = email
        self.password = password
        self.balance = balance

    def login(self, email_, password_):
        if (email_, password_) == (self.email, self.password):
            return True
        return False

    def update_balance(self, amount):
        self.balance = amount


user = User("gosha@roskino.org", "qwerty", 20_000)
print(user.login("gosha@roskino.org", "qwerty123"))
# False
print(user.login("gosha@roskino.org", "qwerty"))
# True
user.update_balance(200)
user.update_balance(-500)
print(user.balance)
# 19700
```

----

#### **Задание 5.2** ####

Определить класс `IntDataFrame`, который принимает список неотрицательных чисел
и приводит к целым значениям все числа в этом списке. После этого становится
доступен метод `count`, который считает количество ненулевых элементов, и метод
`unique`, который возвращает число уникальных элементов.

```python
class IntDataFrame():
    def __init__(self, digit_list):
        self.digit_list = digit_list
        self.to_int()

    def to_int(self):
        for dig, val in enumerate(self.digit_list):
            self.digit_list[dig] = int(self.digit_list[dig])

    def count(self):
        counter = 0
        for num in self.digit_list:
            if num != 0:
                counter += 1
        return counter

    def unique(self):
        return len(set(self.digit_list))


df = IntDataFrame([4.7, 4, 3, 0, 2.4, 0.3, 4])
print(df.count())
# => 5
print(df.unique())
# => 4
```

----
