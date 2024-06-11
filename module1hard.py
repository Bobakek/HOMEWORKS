grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = sorted(students)

new_diction = {}

for student, grade in zip(students_list , grades):
    new_diction[student] = sum(grade) / len(grade)
print(new_diction)
