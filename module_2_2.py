a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))

if a == b and a == c:
    print("3")
elif a==b or a==c or b==c or b==a:
    print('2')
else:
    print('0')
