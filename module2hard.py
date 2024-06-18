def generate_password(n):
    password = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password

def main():
    while True:
        # Вводим число n
        n = int(input("Введите число n (от 3 до 20): "))

        if 3 <= n <= 20:
            break
        else:
            print("Число n должно быть от 3 до 20. Попробуйте снова.")
    password = generate_password(n)
    print(f"{n} - {password}")

if __name__ == "__main__":
    main()
