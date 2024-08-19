# def get_advanced_writer(file_name):
#     def write_everything(*data_set):
#         with open(file_name, 'a') as file:
#             for data in data_set:
#                 file.write(str(data))
#                 file.write('\n')
#     return write_everything
#
#
# write = get_advanced_writer('example.txt')
# write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#CALL
class MysticBall:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third
    def __call__(self):
        words = choice([self.first, self.second, self.third])
        return words + '!'
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


