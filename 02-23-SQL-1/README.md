## Задачи из юнитов модуля SQL-1 (Основы SQL) ##

#### **Задание 1.1** ####

Написать запрос, который выведет из таблицы `kinopoisk` столбцы с названием
фильма, годом его выпуска и рейтингом.

```sql
SELECT movie_title, year, rating FROM sql.kinopoisk
```

----

#### **Задание 1.2** ####

Написать запрос, который выведет из таблицы `kinopoisk` следующие столбцы:

- имя режиссёра (director),
- название фильма (movie_title),
- разница между максимально возможным рейтингом (10) и рейтингом этого фильма.

```sql
SELECT director, movie_title, 10 - rating FROM sql.kinopoisk
```

----