## Задачи из юнитов модуля SQL-3 (Соединение таблиц) ##

### Схема базы sql.teams ###

    id          id команды
    api_id      ключ на таблицу matches
    long_name   полное название команды
    short_name  сокращённое название команды

----

### Схема базы sql.matches ###

    id                  id матча
    season              сезон
    date                дата матча
    home_team_api_id    api_id домашней команды, ключ на таблицу teams
    away_team_api_id    api_id гостевой команды, ключ на таблицу teams
    home_team_goals     количество голов домашней команды
    away_team_goals     количество голов гостевой команды

----

#### **Задание 1.2** ####

Написать запрос, который выведет сезон (`season`), общее количество забитых
мячей домашними (`total_home_goals`) и гостевыми (`total_away_goals`) командами.    
Отсортировать по столбцу с сезоном в порядке возрастания.

```sql
SELECT
    season,
    SUM(home_team_goals) AS total_home_goals,
    SUM(away_team_goals) AS total_away_goals
FROM sql.matches
GROUP BY season
ORDER BY season
```

----

#### **Задание 2.1** ####

Написать запрос, который выведет количество строк соединённой таблицы (декартово
произведение таблиц).

```sql
SELECT
    COUNT(*)
FROM
    sql.teams,
    sql.matches
```

----

#### **Задание 2.2** ####

Написать запрос, который выведет таблицу с результатами матчей, содержащую:

- названия гостевых команд (`long_name`);
- количество забитых мячей домашней команды (`home_team_goals`);
- количество забитых мячей гостевой команды (`away_team_goals`).

```sql
SELECT
    long_name,
    home_team_goals,
    away_team_goals
FROM
    sql.teams,
    sql.matches
WHERE away_team_api_id = api_id
```

----

#### **Задание 3.1** ####

Переписать запрос:

```text
SELECT *
FROM sql.teams, sql.matches
WHERE away_team_api_id = api_id
```

с использованием **`JOIN`**.

```sql
SELECT *
FROM sql.teams
JOIN sql.matches ON away_team_api_id = api_id
```

----

#### **Задание 3.2** ####

Написать запрос, который выведет два столбца: **id** матча (`match_id`) и **id**
домашней команды (`team_id`), а затем отсортировать по **id** матча в порядке
возрастания значений.

```sql
SELECT
    m.id AS match_id,
    t.id AS team_id
FROM sql.teams AS t
JOIN sql.matches AS m ON m.home_team_api_id = t.api_id
ORDER BY match_id
```

----

#### **Задание 3.3** ####

Написать запрос, который выведет столбцы: **id** матча, короткое название
домашней команды (`home_short`), короткое название гостевой команды
(`away_short`).    
Отсортировать запрос по возрастанию **id** матча.

```sql
SELECT
    m.id,
    h.short_name AS home_short,
    a.short_name AS away_short
FROM sql.matches AS m
JOIN sql.teams AS h ON m.home_team_api_id = h.api_id
JOIN sql.teams AS a ON m.away_team_api_id = a.api_id
ORDER BY m.id
```

----

#### **Задание 4.1** ####

Написать запрос, который выведет полное название команды (`long_name`),
количество голов домашней команды (`home_goal`) и количество голов гостевой
команды (`away_goal`) в матчах, где домашней командой были команды с коротким
названием **`GEN`**.    
Отсортировать запрос по **id** матча в порядке возрастания.

```sql
SELECT
    t.long_name,
    m.home_team_goals AS home_goal,
    m.away_team_goals AS away_goal
FROM sql.teams AS t
JOIN sql.matches AS m ON m.home_team_api_id = t.api_id
WHERE t.short_name = 'GEN'
ORDER BY m.id
```

----

#### **Задание 4.2** ####

Написать запрос, чтобы вывести **id** матчей, короткое название домашней
команды (`home_short`), короткое название гостевой команды (`away_short`) для
матчей сезона **2011/2012**, в которых участвовала команда с названием
**Liverpool**.    
Отсортировать по **id** матча в порядке возрастания.

```sql
SELECT
    m.id,
    h.short_name AS home_short,
    a.short_name AS away_short
FROM sql.matches AS m
JOIN sql.teams AS h ON h.api_id = m.home_team_api_id
JOIN sql.teams AS a ON a.api_id = m.away_team_api_id
WHERE
    (
        h.long_name = 'Liverpool'
        OR
        a.long_name = 'Liverpool'
    )
    AND
    m.season = '2011/2012'
ORDER BY m.id
```

----

#### **Задание 4.3** ####

Написать запрос, с помощью которого можно вывести список полных названий команд,
сыгравших в гостях **150** и более матчей.    
Отсортировать список по названию команды.

```sql
SELECT
    t.long_name
FROM sql.teams AS t
JOIN sql.matches AS m ON t.api_id = m.away_team_api_id
GROUP BY t.id
HAVING COUNT(t.api_id = m.away_team_api_id) > 149
ORDER BY t.long_name
```

----

#### **Задание 5.1** ####

Используя `LEFT JOIN`, вывести список уникальных названий команд, содержащихся в
таблице `matches`.    
Отсортировать список в алфавитном порядке.

```sql
SELECT
    DISTINCT t.long_name
FROM sql.teams AS t
LEFT JOIN sql.matches AS m ON
    t.api_id = m.home_team_api_id
    OR
    t.api_id = m.away_team_api_id
WHERE m.id IS NOT NULL
ORDER BY t.long_name
```

----

#### **Задание 5.2** ####

Используя `LEFT JOIN`, написать запрос, который выведет полное название команды
(`long_name`), количество матчей, в которых участвовала команда,&nbsp;&mdash;
домашних и гостевых (`matchess_cnt`).    
Отсортировать по количеству матчей в порядке возрастания, затем&nbsp;&mdash; по
названию команды в алфавитном порядке.

```sql
SELECT
    t.long_name,
    COUNT(m.id) AS matches_cnt
FROM sql.teams AS t
LEFT JOIN sql.matches AS m ON
    t.api_id = m.home_team_api_id
    OR
    t.api_id = m.away_team_api_id
GROUP BY t.id
ORDER BY matches_cnt, t.long_name
```

----

#### **Задание 5.3** ####

Написать запрос, который выведет все возможные уникальные комбинации коротких
названий домашней команды (`home_team`) и коротких названий гостевой команды
(`away_team`).    
Отсортировать запрос по первому и второму столбцам.

```sql
SELECT
    DISTINCT
        t1.short_name AS home_team,
        t2.short_name AS away_team
FROM sql.teams AS t1
CROSS JOIN sql.teams AS t2
ORDER BY home_team, away_team
```

----

#### **Задание 6.1** ####

Написать запрос, который выведет список уникальных полных названий команд
(`long_name`), игравших в гостях в матчах сезона **2012/2013**.    
Отсортировать список в алфавитном порядке.

```sql
SELECT
    DISTINCT t.long_name
FROM sql.teams AS t
JOIN sql.matches AS m ON
    t.api_id = m.away_team_api_id
    AND
    m.season = '2012/2013'
ORDER BY t.long_name
```

----

#### **Задание 6.2** ####

Написать запрос, который выведет полное название команды (`long_name`) и общее
количество матчей (`matches_cnt`), сыгранных командой **Inter** в домашних
матчах.

```sql
SELECT
    t.long_name,
    COUNT(*) AS matches_cnt
FROM sql.teams AS t
JOIN sql.matches AS m ON
    t.api_id = m.home_team_api_id
    AND
    t.long_name = 'Inter'
GROUP BY t.long_name
```

----

#### **Задание 6.3** ####

Написать запрос, который выведет топ-10 команд (`long_name`) по суммарному
количеству забитых голов в гостевых матчах. Во втором столбце запроса вывести
суммарное количество голов в гостевых матчах (`total_goals`).

```sql
SELECT
    t.long_name,
    SUM(m.away_team_goals) AS total_goals
FROM sql.teams AS t
JOIN sql.matches AS m ON
    t.api_id = m.away_team_api_id
GROUP BY t.long_name
ORDER BY total_goals DESC
LIMIT 10
```

----

#### **Задание 6.4** ####

Вывести количество матчей между командами **Real Madrid CF** и **FC Barcelona**.

```sql
SELECT
    COUNT(*)
FROM sql.matches AS m
JOIN sql.teams AS h ON h.api_id = m.home_team_api_id
JOIN sql.teams AS a ON a.api_id = m.away_team_api_id
WHERE
    (
        h.long_name = 'Real Madrid CF'
        AND
        a.long_name = 'FC Barcelona'
    )
    OR
    (
        h.long_name = 'FC Barcelona'
        AND
        a.long_name = 'Real Madrid CF'
    )
```

----

#### **Задание 6.5** ####

Написать запрос, который выведет название команды (`long_name`), сезон
(`season`) и суммарное количество забитых голов в домашних матчах
(`total_goals`). Оставить только те строки, в которых суммарное количество голов
менее десяти.    
Отсортировать запрос по названию команды, а затем по сезону.

```sql
SELECT
    t.long_name,
    m.season,
    SUM(m.home_team_goals) AS total_goals
FROM sql.teams AS t
JOIN sql.matches AS m ON
    t.api_id = m.home_team_api_id
GROUP BY t.long_name, m.season
HAVING SUM(m.home_team_goals) < 10
ORDER BY t.long_name, m.season
```

----
