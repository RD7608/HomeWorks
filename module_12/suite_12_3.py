import unittest
import tests_12_3


# Создание модуля описания объекта TestSuite
test_suite = unittest.TestSuite()

# Добавление тестов RunnerTest и TournamentTest в TestSuite
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

# Создание объекта класса TextTestRunner с аргументом verbosity=2
runner = unittest.TextTestRunner(verbosity=2)

# Запуск тестов
runner.run(test_suite)
