# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# while True:
#     for num in my_list:
#         if num >0:
#             print(num)

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
while num < len(my_list):
    if my_list[num] > 0:
        print(my_list[num])
    num +=1
