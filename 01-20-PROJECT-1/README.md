# Анализ вакансий из HeadHunter #

## (Преобразование, исследование и очистка данных) ##

### Содержание ###

[1. Организационная информация](#организационная-информация)    
[2. Требования к оформлению](#требования-к-оформлению)    
[3. Важные замечания для воспроизведения проекта](#важные-замечания-для-воспроизведения-проекта)    
[4. Результат](#результат)    

### Организационная информация ###

Проект состоит из четырёх частей:

1. Базовый анализ структуры данных
2. Преобразование данных
3. Разведывательный анализ
4. Очистка данных

Каждая часть состоит из блока практических заданий, которые необходимо выполнить
в своих jupyter-ноутбуках, и контрольных вопросов на платформе. Задания
выполняются последовательно.

Помимо проверки заданий на платформе, предстоит отправить свой код ментору для
code-ревью. Будет предоставлен ноутбук-шаблон и требования, согласно которым
нужно оформить своё решение.

[:arrow_up: Содержание](#содержание)

----

### Требования к оформлению ###

- Решение оформляется только в `Jupyter Notebook`.

- Решение оформляется в соответствии с ноутбуком-шаблоном.

- Каждое задание выполняется в отдельной ячейке, выделенной под задание (в
шаблоне они помечены как `#ваш код здесь`). Не следует создавать множество ячеек
для решения задачи&nbsp;&mdash; это создаёт неудобства при проверке.

- Код для каждого задания оформляется в одной-двух jupyter-ячейках (не стоит
создавать множество ячеек для решения задачи, это усложняет проверку).

- Решение должно использовать только пройденный материал: переменные, основные
структуры данных (списки, словари, множества), циклы, функции, библиотеки
`numpy`, `pandas`, `matplotlib`, `seaborn`, `plotly`. Если кто-то думает, что
для решения необходимо воспользоваться сторонними библиотеками или инструментами
(например `Excel`), другими языками программирования или неизученными
конструкциями, этот &laquo;кто-то&raquo; сильно ошибается :wink:. Все задания
решаются с помощью уже знакомых методов.

- Код должен быть читаемым и понятным: имена переменных и функций отражают их
сущность, важно избегать многострочных конструкций и условий.

- Пользоваться руководством [PEP-8](https://peps.python.org/pep-0008/).

- Графики оформляются в соответствии с теми правилами, которые приведены в
модуле по визуализации данных.

- **Обязательное требование:** графики должны содержать название, отражающее их
суть, и подписи осей.

- Выводы к графикам оформляются в формате `Markdown` под самим графиком в
отдельной ячейке (в шаблоне они помечены как `ваши выводы здесь`). Выводы должны
быть представлены в виде небольших связанных предложений на русском языке.

[:arrow_up: Содержание](#содержание)

----

### Важные замечания для воспроизведения проекта ###

1. :warning: **GitHub** не позволяет выложить в репозиторий датасет, размер
которого превышает 25 Мб. Файл с данными весит более 450 Мб. Поэтому для
воспроизведения работы файла проекта
**:computer:/:file_folder:/Project-1.ipynb** его надо скачать [по ссылке на
[Google Disk](https://drive.google.com/file/d/1ZQ4Q8SnRWJVNICl6GDzOPZfCaRezgT4O/view?usp=sharing)
и поместить в директорию **:computer:/:file_folder:/data/**. Туда же можно
поместить скачанный [по ссылке на Google Disk](https://drive.google.com/file/d/1eYtSav-oSzK49fsNbdK6fnIXF96_dDel/view?usp=sharing) файл с выгрузкой курсов валют (также он есть в данном репозитории).

2. GitHub не поддерживает отображение интерактивной визуализации в `Plotly`.
Графики, построенные с помощью `Plotly`, могут не отображаться на странице
репозитория.    
**Базовое решение проблемы:** создать в проекте директорию, в которой
сохраняются построенные графики в формате HTML (данный метод разобран в модуле
по визуализации данных). Так можно просматривать графики через GitHub, открывая
файлы в браузере.

[:arrow_up: Содержание](#содержание)

----

### Результат ###

[**`Project-1.ipynb`**](Project-1.ipynb)&nbsp;&mdash; Файл в формате ноутбука с
решениями.

Все графики построены без использования `Plotly`, а для ответов на вопросы
заданий в исполняемые ячейки добавлен код для текстового вывода сведений,
которые можно было бы получить из интерактивных графиков `Plotly`.

[:arrow_up: Содержание](#содержание)

----