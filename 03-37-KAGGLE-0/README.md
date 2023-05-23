# Соревнование на Kaggle #

![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=plastic&logo=kaggle&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=plastic&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=plastic&logo=pandas&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=plastic&logo=PyTorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=plastic&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=plastic&logo=Matplotlib&logoColor=black)
**`Seaborn`**
**`LightAutoML`**

## Predict car price (Предсказание стоимости подержанного автомобиля) ##

[Ссылка на соревнование](https://www.kaggle.com/competitions/sf-dst-predict-car-price)

### Содержание ###

[1. Условия соревнования](#условия-соревнования)    
[2. Файлы датасета](#файлы-датасета)    
[3. Описание признаков](#описание-признаков)    
[4. Решение](#решение)    

### Условия соревнования ###

1. Построить модель для предсказания адекватной стоимости машины по её
характеристикам из объявления.
2. Тестовая выборка представлена в Лидерборде целиком. Поэтому лучшие и победные
решения буду проверяться на их &laquo;адекватность&raquo; (чтоб не было подгонки
под тестовую выборку).
3. Разрешено использовать любые ML-алгоритмы и библиотеки (кроме DL).
4. Делаем реальный ML продукт, который потом сможет нормально работать на новых
данных.
5. Метрикой в данном соревновании является **MAE (mean absolute error)**&nbsp;&mdash;
среднее абсолютное отклонение.
6. Сабмит в соревнование должен выглядеть как файл `sample_submission.csv`&nbsp;&mdash;
содержать 10697 строк с предсказаниями для каждого `row_ID` от 35000 до 45696
включительно.

[:arrow_up: Содержание](#содержание)

----

### Файлы датасета ###

[**`data/sf-dst-predict-car-price.zip`**](data/sf-dst-predict-car-price.zip)&nbsp;&mdash;
архив с файлами:

- **`train_data.csv`**&nbsp;&mdash; обучающая выборка
- **`test_data.csv`**&nbsp;&mdash; данные, на которых надо делать предсказание.
Не содержат в себе целевую переменную `final_price`.
- **`sample_submission.csv`**&nbsp;&mdash; результирующий файл для Submission.

----

### Описание признаков ###

- **`row_id`**&nbsp;&mdash; ID объявления
- **`vehicle_manufacturer`**&nbsp;&mdash; марка автомобиля
- **`vehicle_model`**&nbsp;&mdash; модель автомобиля
- **`vehicle_category`**&nbsp;&mdash; тип машины
- **`current_mileage`**&nbsp;&mdash; текущий пробег
- **`vehicle_year`**&nbsp;&mdash; год выпуска
- **`vehicle_gearbox_type`**&nbsp;&mdash; тип коробки передач
- **`doors_cnt`**&nbsp;&mdash; количество дверей
- **`wheels`**&nbsp;&mdash; левый/правый руль
- **`vehicle_color`**&nbsp;&mdash; цвет машины
- **`vehicle_interior_color`**&nbsp;&mdash; цвет салона машины
- **`car_vin`**&nbsp;&mdash; VIN номер автомобиля
- **`car_leather_interior`**&nbsp;&mdash; флаг наличия кожаного салоона
- **`deal_type`**&nbsp;&mdash; тип объявления: продажа или аренда
- **`final_price`**&nbsp;&mdash; стоимость машины (**Целевая переменная**)

----

### Решение ###

- [**`module.ipynb`**](module.ipynb)&nbsp;&mdash; черновик для соревнований на Kaggle.
- [**`output/sample_submission`**](output/sample_submission.csv)&nbsp;&mdash;
submission-файл, участвующий в соревнованиях.

----
