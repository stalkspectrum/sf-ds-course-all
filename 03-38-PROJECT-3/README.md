<h2 align="center">:gb: Disclaimer</h2>

:warning: This test project was performed for a company with predominantly
Russian-speaking specialists. Therefore, all explanations, comments and other
texts are provided exclusively in Russian.

----

# Exploratory Data Analysis and Feature Engineering #

## (Соревнование на Kaggle) ##

[Ссылка на соревнование](https://www.kaggle.com/competitions/sf-booking)

[Профиль на Kaggle&nbsp;&mdash; **Ded Wildfield**](https://www.kaggle.com/wildfielded)

![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=plastic&logo=kaggle&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=plastic&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=plastic&logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=plastic&logo=scipy&logoColor=%white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=plastic&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=plastic&logo=Matplotlib&logoColor=black)
**`Seaborn`**
**`NLTK`**

### Содержание ###

[1. Смоделированная ситуация](#смоделированная-ситуация)    
[2. Описание датасета](#описание-датасета)    
[3. Требования к оформлению](#требования-к-оформлению)    
[4. Критерии оценивания](#критерии-оценивания)    
[5. Результат](#результат)    

### Смоделированная ситуация ###

Одна из проблем компании Booking&nbsp;&mdash; это нечестные отели, которые
накручивают себе рейтинг. Одним из способов обнаружения таких отелей является
построение модели, которая предсказывает рейтинг отеля. Если предсказания модели
сильно отличаются от фактического результата, то, возможно, отель ведёт себя
нечестно, и его стоит проверить. Поставлена задача создать такую модель.

Предстоит работать с датасетом, в котором содержатся сведения о 515000 отзывах
на отели Европы. Модель, которую надо обучить, должна предсказывать рейтинг
отеля по данным сайта Booking на основе имеющихся в датасете данных.

[:arrow_up: Содержание](#содержание)

----

### Описание датасета ###

**Скачиваемые файлы:**

- [**`hotels_train.csv.zip`**](https://drive.google.com/file/d/10PTV3z7bLPkjHc_OVanKtCFEDSS7z1Tn/view?usp=sharing)&nbsp;&mdash;
набор данных для обучения;
- [**`hotels_test.csv.zip`**](https://drive.google.com/file/d/1nUwezJ5sjMQ50br_L8Ehqr-TJaXksxZ9/view?usp=sharing)&nbsp;&mdash;
набор данных для оценки качества;
- [**`submission.csv.zip`**](https://drive.google.com/file/d/1t61EtcNUiriFcNiJxP-PpLwFKZMMl8Q_/view?usp=sharing)&nbsp;&mdash;
результирующий файл для Submission.

**Датасет содержит 17 полей со следующей информацией:**

1. **`hotel_address`**&nbsp;&mdash; адрес отеля;
2. **`review_date`**&nbsp;&mdash; дата, когда рецензент разместил соответствующий
отзыв;
3. **`average_score`**&nbsp;&mdash; средний балл отеля, рассчитанный на основе
последнего комментария за последний год;
4. **`hotel_name`**&nbsp;&mdash; название отеля;
5. **`reviewer_nationality`**&nbsp;&mdash; страна рецензента;
6. **`negative_review`**&nbsp;&mdash; отрицательный отзыв, который рецензент дал
отелю;
7. **`review_total_negative_word_counts`**&nbsp;&mdash; общее количество слов в
отрицательном отзыве;
8. **`positive_review`**&nbsp;&mdash; положительный отзыв, который рецензент дал
отелю;
9. **`review_total_positive_word_counts`**&nbsp;&mdash; общее количество слов в
положительном отзыве.
10. **`reviewer_score`**&nbsp;&mdash; оценка, которую рецензент поставил отелю на
основе своего опыта;
11. **`total_number_of_reviews_reviewer_has_given`**&nbsp;&mdash; количество
отзывов, которые рецензенты дали в прошлом;
12. **`total_number_of_reviews`**&nbsp;&mdash; общее количество действительных
отзывов об отеле;
13. **`tags`**&nbsp;&mdash; теги, которые рецензент дал отелю;
14. **`days_since_review`**&nbsp;&mdash; количество дней между датой проверки и
датой очистки;
15. **`additional_number_of_scoring`**&nbsp;&mdash; есть также некоторые гости,
которые просто поставили оценку сервису, но не оставили отзыв. Это число
указывает, сколько там действительных оценок без проверки;
16. **`lat`**&nbsp;&mdash; географическая широта отеля;
17. **`lng`**&nbsp;&mdash; географическая долгота отеля.

[:arrow_up: Содержание](#содержание)

----

### Требования к оформлению ###

- Результаты соревнования оцениваются по метрике MAPE.
- Результирующий файл `submission.csv`, где для каждого **id** отеля в наборе
тестовых данных нужно предсказать рейтинг отеля в переменной **reviewer_score**.
Файл должен содержать заголовок и иметь следующий формат:

```text
reviewer_score,id
1,1
```

[:arrow_up: Содержание](#содержание)

----

### Критерии оценивания ###

1. Качество кода (соблюдение стандартов оформления PEP-8, комментирование кода,
README к проекту). Оформление проекта на GitHub, GitLab, Kaggle;
2. Очистка данных;
3. Исследование данных (качество визуализации, наличие идей, гипотез,
комментариев);
4. Генерация признаков;
5. Отбор признаков;
6. Преобразование признаков;
7. Качество решения: результат метрики MAPE.

[:arrow_up: Содержание](#содержание)

----

### Результат ###

[**`WF_BookingPro`**](https://www.kaggle.com/code/wildfielded/wf-bookingpro)&nbsp;&mdash;
Notebook на Kaggle.com.

[**`Project-3.ipynb`**](Project-3.ipynb)&nbsp;&mdash; Черновой (и более
подробный) вариант решения.

[**`output/submission.csv`**](output/submission.csv)&nbsp;&mdash; Файл
предсказаний.

[:arrow_up: Содержание](#содержание)

----
