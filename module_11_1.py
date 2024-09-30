import requests
import pandas as pd
import numpy as np

#request
# GET-запрос к API и вывод данных
#Основные возможности:
# Отправка GET-запросов.
# Работа с JSON-ответами.
# Обработка статусов HTTP-ответов.
# Библиотека предоставляет простой и интуитивно понятный интерфейс для работы с веб-данными, позволяя легко интегрироваться с API.
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# if response.status_code == 200:
#     data = response.json()
#     print("First post title:", data[0]['title'])
# else:
#     print("Error:", response.status_code)

# PANDAS. Основные возможности:
# Чтение и запись данных.
# Фильтрация и группировка данных.
# Быстрый анализ данных.
# Чтение данных из CSV
#Pandas значительно упрощает процесс анализа и обработки больших объемов данных, предоставляя высокоуровневые инструменты для манипуляций с данными.
#чтение данных из exel
# data = pd.read_csv('data.csv')
#
# # Простая фильтрация данных
# filtered_data = data[data['age'] > 30]
#
# # Группировка данных и вывод среднего значения
# grouped_data = data.groupby('city')['salary'].mean()
# print(grouped_data)

# Numpy — это библиотека для работы с многомерными массивами и выполнения высокоэффективных математических операций.
# Основные возможности:
# Создание массивов.
# Математические операции с элементами массивов.
# Матричные вычисления.
# Создание массива
arr = np.array([1, 2, 3, 4, 5])

# Операция умножения на скаляр
arr_scaled = arr * 10
print("Scaled array:", arr_scaled)

# Вычисление среднего значения
mean_value = np.mean(arr)
print("Mean value:", mean_value)

# Создание матрицы и её транспонирование
matrix = np.array([[1, 2], [3, 4]])
transposed = np.transpose(matrix)
print("Transposed matrix:\n", transposed)
#Numpy значительно расширяет возможности Python для работы с численными данными и выполнением научных расчетов.
