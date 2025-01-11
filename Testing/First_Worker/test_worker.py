from unittest import TestCase, main

from Testing.First_Worker.worker import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker('Elena', 1000, 100)

    def test_correct_init(self):

        self.assertEqual('Elena', self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_with_positive_energy_increases_money_and_decreases_energy(self):
        expected_money = self.worker.money + self.worker.salary
        expected_energy = self.worker.energy - 1

        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_work_with_negative_energy_raises_exception(self):
        self.worker.energy = -1

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_rest_should_increase_energy(self):

        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_return_string(self):

        self.assertEqual('Elena has saved 0 money.', self.worker.get_info())

if __name__ == '__main__':
    main()
