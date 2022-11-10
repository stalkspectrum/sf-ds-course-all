## Задачи из юнитов модуля SQL-5 (Типы данных) ##

### Схема базы sql.city ###

    city_id     INTEGER     уникальный идентификатор города, первичный ключ
    city_name   TEXT        название города
    state       TEXT        штат, к которому относится город
    population  INTEGER     население города
    area        NUMERIC     площадь города

----

### Схема базы sql.customer ###

    cust_id         INTEGER     уникальный идентификатор клиента, первичный ключ
    cust_name       TEXT        название клиента
    annual_revenue  NUMERIC     ежегодная выручка
    cust_type       TEXT        тип пользователя
    address         TEXT        адрес
    zip             INTEGER     почтовый индекс
    phone           TEXT        телефон
    city_id         INTEGER     идентификатор города, внешний ключ к таблице city

----

### Схема базы sql.driver ###

    driver_id       INTEGER     уникальный идентификатор водителя, первичный ключ
    first_name      TEXT        имя водителя
    last_name       TEXT        фамилия водителя
    address         TEXT        адрес водителя
    zip_code        INTEGER     почтовый индекс водителя
    phone           TEXT        телефон водителя
    city_id         INTEGER     идентификатор города водителя, внешний ключ
                                к таблице city

----

### Схема базы sql.shipment ###

    ship_id     INTEGER     уникальный идентификатор доставки, первичный ключ
    cust_id     INTEGER     идентификатор клиента, которому отправлена доставка,
                            внешний ключ к таблице customer
    weight      NUMERIC     вес посылки
    truck_id    INTEGER     идентификатор грузовика, на котором отправлена доставка,
                            внешний ключ к таблице truck
    driver_id   INTEGER     идентификатор водителя, который осуществлял доставку,
                            внешний ключ к таблице driver
    city_id     INTEGER     идентификатор города в который совершена доставка,
                            внешний ключ к таблице city
    ship_date   DATE        дата доставки

----

#### **Задание 3.1** ####

Узнать, сколько сейчас времени в другом регионе, например Лос-Анджелесе.
Написать запрос, который выведет текущие время и дату в часовом поясе
Лос-Анджелеса (`'America/Los_Angeles'`). Столбец в выдаче&nbsp;&mdash; **now**
(время и дата в нужном часовом поясе).

```sql
SELECT NOW() AT TIME ZONE 'America/Los_Angeles' AS now
```

----

#### **Задание 3.2** ####

Предположим, есть дата и время какого-то события и надо посмотреть, к какой дате
оно относится для Москвы и для UTC. Использовать подзапрос

```text
with x as 
(
select '2018-12-31 21:00:00+00'::timestamp with time zone ts
)
```

и вывести дату в **ts** в Московском часовом поясе и в поясе UTC. Столбцы в
выдаче: `dt_msk` (дата в московском часовом поясе), `dt_utc` (дата в UTC).

```sql
```

----