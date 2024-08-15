# def apply_all_func(int_list, *functions):
#     result = [] # list to store the result
#     for i in functions:
#         result.append((i.__name__, i(int_list)))

#     return result

# print(apply_all_func([6, 20, 15, 9], max, min))
# print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

def apply_all_func(int_list, *functions):
    result = {}  # Используем словарь для хранения результатов
    for func in functions:
        result[func.__name__] = func(int_list)
    return result

# Примеры вызова функции
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
