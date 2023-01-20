## Некоторые термины и определения модуля EDA-5 (A/B-тестирование) ##

**A/B-тестирование**&nbsp;&mdash; сравнение текущей версии продукта (версии
**`А`**) с его изменённой версией (версией **`B`**) на основании данных,
полученных до введения.

----

**Ошибка I рода**&nbsp;&mdash; Отбросить верную $H_0$ (нулевую гипотезу).

Например, на основе полученных данных можно принять решение, что вариант **`B`**
является более предпочтительным, однако такая разница была обусловлена лишь
случайностью или внешними факторами.

----

**Ошибка II рода**&nbsp;&mdash; Принять неверную $H_0$ (нулевую гипотезу).

Например, на основе полученных данных можно принять решение, что для
пользователей нет разницы между вариантами **`А`** и **`В`**, хотя на самом деле
произведено некорректное сравнение и вариант **`В`** был лучшим.

----

**Этапы A/B-тестирования**

1. Определение метрик и выдвижение гипотезы
2. Подготовка к тестированию
3. Настройка распределения на группы
4. Проверка корректности эксперимента
5. Сбор результатов
6. Анализ результатов
7. Формулирование выводов и принятие решения

----

**Проблема подглядывания**&nbsp;&mdash; ошибочное принятие решения о
статистической значимости результатов до ожидания окончания статистического
теста.

----