import unittest
from runner import Runner
from runner import Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        # Создаем трех бегунов
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        # Выводим результаты всех тестов
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_race_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results["Usain vs Nick"] = results
        # Проверяем, что Ник последний
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_race_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results["Andrey vs Nick"] = results
        # Проверяем, что Ник последний
        self.assertTrue(results[max(results.keys())].name == "Ник")

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results["Usain vs Andrey vs Nick"] = results
        # Проверяем, что Ник последний
        self.assertTrue(results[max(results.keys())].name == "Ник")


if __name__ == "__main__":
    unittest.main()
