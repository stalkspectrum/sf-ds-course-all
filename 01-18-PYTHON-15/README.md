## Задачи из юнитов модуля PYTHON-15 (ООП) ##

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
