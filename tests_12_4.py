import unittest
import logging
from rt_with_exceptions import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        logging.info('Тестирование класса RunnerTest началось.')

    def setUp(self):
        self.usain = Runner("Usain", speed=10)

    def tearDown(self):
        logging.info('Тест завершён.')

    def test_walk(self):
        try:
            # Передаем отрицательное значение в speed для проверки
            runner = Runner("TestRunner", speed=-5)
            for _ in range(10):
                runner.walk()

            self.assertEqual(runner.distance, 50)  # Ожидаем ошибку
            logging.info('"test_walk" выполнен успешно')

        except ValueError as e:
            logging.warning('Неверная скорость для Runner: %s', e)

    def test_run(self):
        try:
            # Передаем неверный тип данных в name для проверки
            runner = Runner(12345, speed=10)
            for _ in range(10):
                runner.run()

            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')

        except TypeError as e:
            logging.warning('Неверный тип данных для объекта Runner: %s', e)

    @classmethod
    def tearDownClass(cls):
        logging.info('Все тесты класса RunnerTest завершены.')

if __name__ == "__main__":
    unittest.main()
