from threading import Thread, Lock
from time import sleep
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            deposit_amount = randint(50, 100)
            with self.lock:

                self.balance += deposit_amount
                print(f'Депозит: {deposit_amount}, Баланс: {self.balance}')
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            take_amount = randint(50, 500)
            print(f'запрос на вывод: {take_amount}, Баланс: {self.balance}')
            with self.lock:

                if take_amount <= self.balance:
                    self.balance -= take_amount
                    print(f'Снятие: {take_amount}, Баланс: {self.balance}')
                else:
                    print(f'Недостаточно средств для снятия {take_amount}. Текущий баланс: {self.balance}')
                    self.lock.acquire()
            sleep(0.001)

bk = Bank()

# Создание и запуск потоков
th1 = Thread(target=bk.deposit)
th2 = Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
