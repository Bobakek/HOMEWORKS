def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с разным количеством аргументов
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# Создание списка и словаря
values_list = [42, 'another string', False]
values_dict = {'a': 99, 'b': 'hello', 'c': [7, 8, 9]}

# Передача списка и словаря в функцию с распаковкой
print_params(*values_list)
print_params(**values_dict)

# Создание списка с двумя элементами
values_list_2 = [54.32, 'Строка']

# Передача списка с распаковкой и дополнительным параметром
print_params(*values_list_2, 42)
