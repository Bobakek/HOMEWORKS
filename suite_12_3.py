import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создаем TestSuite
suite = unittest.TestSuite()

# Добавляем тесты в TestSuite
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

# Запускаем TestSuite
if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
