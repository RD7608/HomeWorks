import unittest


def freeze_test(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest(f'Тесты в этом кейсе заморожены')
        else:
            return func(self, *args, **kwargs)
    return wrapper


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @freeze_test
    def test_walk(self):
        runner = Runner('Runner')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @freeze_test
    def test_run(self):
        runner = Runner('Runner')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @freeze_test
    def test_challenge(self):
        runner1 = Runner('Runner 1')
        runner2 = Runner('Runner 2')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                # Сортировка оставшихся участников по оставшемуся расстоянию
                self.participants.sort(key=lambda x: self.full_distance - x.distance, reverse=True)

        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in sorted(cls.all_results.items()):
            # print(value)     # отображается ({1: <tests_12_2.Runner object at 0x00000294FCD7D040>})
            result = {k: v.name for k, v in value.items()}
            print(result)

    @freeze_test
    def test_race_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.assertTrue(results[len(results)] == self.nick)
        self.all_results["1"] = results

    @freeze_test
    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.assertTrue(results[len(results)] == self.nick)
        self.all_results["2"] = results

    @freeze_test
    def test_race_all(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.assertTrue(results[len(results)] == self.nick)
        self.all_results["3"] = results
