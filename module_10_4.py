import threading
import time
import random
from queue import Queue

# Класс Table
class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None  # Гость за столом, по умолчанию None

# Класс Guest, наследуемый от класса Thread
class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    # Метод run для эмуляции ожидания приема пищи
    def run(self):
        time_to_eat = random.randint(3, 10)  # Случайное время ожидания от 3 до 10 секунд
        time.sleep(time_to_eat)  # Гость "ест" в течение этого времени

# Класс Cafe
class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)  # Список столов
        self.queue = Queue()  # Очередь для гостей

    # Метод прибытия гостей
    def guest_arrival(self, *guests):
        for guest in guests:
            # Найти свободный стол
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                # Сажаем гостя за стол
                free_table.guest = guest
                guest.start()  # Запускаем поток гостя
                print(f'{guest.name} сел(-а) за стол номер {free_table.number}')
            else:
                # Если столов нет, ставим гостя в очередь
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    # Метод обслуживания гостей
    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():  # Гость закончил прием пищи
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None  # Освобождаем стол

                # Проверяем, есть ли гости в очереди и свободные столы
                if table.guest is None and not self.queue.empty():
                    next_guest = self.queue.get()  # Получаем гостя из очереди
                    table.guest = next_guest
                    next_guest.start()  # Запускаем поток нового гостя
                    print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')

            time.sleep(1)  # Небольшая задержка для имитации обслуживания

# Пример использования программы:
if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]

    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]

    # Создание гостей
    guests = [Guest(name) for name in guests_names]

    # Заполнение кафе столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()
