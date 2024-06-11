
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество студентов в отсортированный список
sorted_students = sorted(students)

# Создаём пустой словарь для хранения имени ученика и его среднего балла
average_grades = {}

# Заполняем словарь средними баллами
for student, grades_list in zip(sorted_students, grades):
    average_grades[student] = sum(grades_list) / len(grades_list)

# Выводим получившийся словарь
print(average_grades)
