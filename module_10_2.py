from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100

    def run(self):
        print(self.name, "на нас напали!")
        days = 0
        while self.enemy > 0:
            sleep(1)
            days += 1
            self.enemy -= self.power

            if self.enemy > 0:
                print(f"{self.name} сражается {days} день(дня) ..., осталось {self.enemy} воинов.")
            else:
                print(f'{self.name} победил! спустя {days} день(дня)...')
                break

# Создание объектов класса Knight
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения обоих потоков
first_knight.join()
second_knight.join()

print("Битвы завершены.")

