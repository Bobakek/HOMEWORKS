import unittest
from functools import wraps
from runner import Runner, Tournament


# Декоратор для пропуска тестов, если is_frozen=True
def skip_if_frozen(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)
    return wrapper

# Класс RunnerTest
class RunnerTest(unittest.TestCase):
    is_frozen = False  # Можно изменить на True для заморозки тестов

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrew = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @skip_if_frozen
    def test_walk(self):
        for _ in range(10):
            self.usain.walk()
        # Учитываем, что walk увеличивает дистанцию на speed (10 * 10 = 100)
        self.assertEqual(self.usain.distance, 100)

    @skip_if_frozen
    def test_run(self):
        for _ in range(10):
            self.usain.run()
        # Учитываем, что run увеличивает дистанцию на speed * 2 (10 * 20 = 200)
        self.assertEqual(self.usain.distance, 200)

    @skip_if_frozen
    def test_challenge(self):
        tour = Tournament(90, self.usain, self.nick)
        results = tour.start()
        self.assertEqual(results[2], self.nick)

# Класс TournamentTest
class TournamentTest(unittest.TestCase):
    is_frozen = True  # Устанавливаем в True для заморозки всех тестов

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrew = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @skip_if_frozen
    def test_first_tournament(self):
        tour = Tournament(90, self.usain, self.nick)
        results = tour.start()
        self.assertEqual(results[2], self.nick)

    @skip_if_frozen
    def test_second_tournament(self):
        tour = Tournament(90, self.andrew, self.nick)
        results = tour.start()
        self.assertEqual(results[2], self.nick)

    @skip_if_frozen
    def test_third_tournament(self):
        tour = Tournament(90, self.usain, self.andrew, self.nick)
        results = tour.start()
        self.assertEqual(results[3], self.nick)
