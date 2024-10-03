import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('John')

        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)


    def test_run(self):
        runner = Runner('John')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner = Runner('John')
        runner1 = Runner('NIK')
        for i in range(10):
            runner1.run()
            runner.walk()
        self.assertNotEqual(runner1.distance, runner.walk())


if __name__ == '__main__':
    unittest.main()

