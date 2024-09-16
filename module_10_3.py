import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.locked = False 

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f'Пополнение: {amount}. Баланс: {self.balance}')
                # Разблокируем поток, если баланс >= 500 и был заблокирован
                if self.balance >= 500 and self.locked:
                    print("Баланс восстановлен, разблокировка...")
                    self.locked = False
            time.sleep(0.001)  # Имитация задержки

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f'Запрос на {amount}')
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'Снятие: {amount}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
                    # Блокируем поток, если баланс недостаточен
                    if not self.locked:
                        print("Блокировка операций снятия...")
                        self.locked = True
            time.sleep(0.001)  # Имитация задержки


# Создаем объект банка
bk = Bank()

# Создаем два потока для пополнения и снятия
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запускаем потоки
th1.start()
th2.start()

# Ожидаем завершения потоков
th1.join()
th2.join()

# Выводим итоговый баланс
print(f'Итоговый баланс: {bk.balance}')

