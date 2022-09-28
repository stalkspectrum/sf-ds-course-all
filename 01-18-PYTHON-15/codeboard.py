'''
Задание 4.1
Дописать определение класса DepartmentReport, который выводит отчёт по отделам
компании. У него должны быть определены:
- атрибут revenues — список, где мы храним значения выручки отделов;
- метод add_revenue, который добавляет выручку одного отдела;
- метод average_revenue, который возвращает среднюю выручку по всем отделам.
'''
class DepartmentReport_():
    def add_revenue(self, amount):
        if not hasattr(self, 'revenues'):
            self.revenues = []
        self.revenues.append(amount)

    def average_revenue(self):
        return sum(self.revenues) / len(self.revenues)

report = DepartmentReport_()
report.add_revenue(1_000_000)
report.add_revenue(400_000)
print(report.revenues)
# => [1000000, 400000]
print(report.average_revenue())
# => 700000.0


'''
Задание 4.2
Улучшить класс DepartmentReport. Класс при инициализации должен принимать
переменную company и инициализировать её значением атрибут company, а также
инициализировать атрибут revenues пустым списком.
Метод average_revenue должен возвращать строку
"Average department revenue for (company_name): (average_revenue)".
'''
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
# => Average department revenue for Danon: 700000


'''
Задание 5.1
Определить класс для пользователей User:
- у него должны быть атрибуты email, password и balance, которые устанавливаются
при инициализации;
- у него должен быть метод login, который принимает емайл и пароль. Если они
совпадают с атрибутами объекта, он возвращает True, а иначе — False;
- должен быть метод update_balance(amount), который изменяет баланс счёта на
величину amount.
'''
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
        self.balance += amount


user = User("gosha@roskino.org", "qwerty", 20_000)
print(user.login("gosha@roskino.org", "qwerty123"))
# => False
print(user.login("gosha@roskino.org", "qwerty"))
# => True
user.update_balance(200)
user.update_balance(-500)
print(user.balance)
# => 19700


'''
Задание 5.2
Определить класс IntDataFrame, который принимает список неотрицательных чисел и
приводит к целым значениям все числа в этом списке. После этого становится
доступен метод count, который считает количество ненулевых элементов, и метод
unique, который возвращает число уникальных элементов.
'''
class IntDataFrame():
    def __init__(self, dig_list):
        self.dig_list = dig_list
        self.to_int()

    def to_int(self):
        for n, value in enumerate(self.dig_list):
            self.dig_list[n] = int(self.dig_list[n])

    def count(self):
        counter = 0
        for m in self.dig_list:
            if m != 0:
                counter += 1
        return counter

    def unique(self):
        return len(set(self.dig_list))


df = IntDataFrame([4.7, 4, 3, 0, 2.4, 0.3, 4])
print(df.count())
# => 5
print(df.unique())
# => 4


'''
Задание 5.3
Написать класс сборщика технических сообщений OwnLogger.
- У него должен быть метод log(message, level), который записывает сообщения.
Здесь сообщение message может быть любым, а level — один из
"info", "warning", "error".
- Также применить метод show_last(level), где level может быть "info",
"warning", "error", "all". Для "all" он просто возвращает последнее добавленное
сообщение, а для остальных - последнее поступившее сообщение соответствующего
уровня.
- При этом по умолчанию значение именно "all". Если подходящего сообщения нет,
возвращает None.
'''
class OwnLogger():
    def __init__(self):
        self.log_list = []

    def log(self, message, level):
        self.log_list.append((message, level))

    def show_last(self, level='all'):
        for log_tup in self.log_list[-1::-1]:
            if level == 'all':
                return log_tup[0]
            else:
                if log_tup[1] == level:
                    return log_tup[0]
        return None


logger = OwnLogger()
logger.log("System started", "info")
print(logger.show_last("error"))
# => None
logger.log("Connection instable", "warning")
logger.log("Connection lost", "error")

print(logger.show_last())
# => Connection lost
print(logger.show_last("info"))
# => System started


'''
Задание 7.3
Задание на самопроверку.

Сделать функцию, которая принимает от пользователя путь и выводит всю информацию
о содержимом этой папки. Для реализации используйте функцию встроенного модуля
os.walk(). Если путь не указан, то сравнение начинается с текущей директории.
'''


'''
Задание 7.4
Задание на самопроверку.

Создать любой файл на операционной системе под название input.txt и построчно
перепишите его в файл output.txt.
'''


'''
Задание 7.5
Задание на самопроверку.

Дан файл numbers.txt, компоненты которого являются действительными числами
(файл создать самостоятельно и заполнить любыми числам, в одной строке одно
число). Найти сумму наибольшего и наименьшего из значений и записать результат в
файл output.txt.
'''


'''
Задание 7.6
Задание на самопроверку.

В текстовый файл построчно записаны фамилии и имена учащихся класса и их оценки
за контрольную. Подсчитать количество учащихся, чья оценка меньше 3 баллов.
Cодержание файла:

Иванов О. 4
Петров И. 3
Дмитриев Н. 2
Смирнова О. 4
Керченских В. 5
Котов Д. 2
Бирюкова Н. 1
Данилов П. 3
Аранских В. 5
Лемонов Ю. 2
Олегова К. 4
'''


'''
Задание 7.7
Задание на самопроверку.

Выполнить реверсирование строк файла (перестановку строк файла в обратном
порядке).
'''


'''
Задание 8.7
Задание на самопроверку.

Создать скрипт, который будет в input() принимать строки, и их необходимо будет
конвертировать в числа, добавить try-except на то, чтобы строки могли быть
сконвертированы в числа.
В случае удачного выполнения скрипта написать: «Вы ввели <введённое число>».
В конце скрипта обязательно написать: «Выход из программы».
ПРИМЕЧАНИЕ: Для отлова ошибок использовать try-except, а также блоки finally и
else.

Примеры входов и выходов:

Входные данные      Выходные данные

1                   Вы ввели 1
                                Выход из программы

-3                  Вы ввели -3
                                Выход из программы

razdvatri           Вы ввели неправильное число
                                Выход из программы
'''


'''
Задание 9.5
Задание на самопроверку.

Создать класс Square. Добавить в конструктор класса Square собственное
исключение NonPositiveDigitException, унаследованное от ValueError, которое
будет срабатывать каждый раз, когда сторона квадрата меньше или равна 0.
'''
