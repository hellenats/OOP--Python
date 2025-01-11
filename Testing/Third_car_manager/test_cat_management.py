from unittest import TestCase, main

from Third_car_manager.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car('Porsche', '911', 10, 100)

    def test_correct_init(self):

        self.assertEqual('Porsche', self.car.make)
        self.assertEqual('911', self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_empty_string_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_empty_string_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_negative_value_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_negative_value_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_with_negative_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_or_negative_fuel_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_excessive_fuel_should_not_exceed_fuel_capacity(self):

        self.car.refuel(120)

        self.assertEqual(100, self.car.fuel_amount)

    def test_drive_with_not_enough_fuel_amount_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.drive(50)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_enough_fuel_should_decrease_fuel_amount(self):

        self.car.fuel_amount = 60

        self.car.drive(50)

        self.assertEqual(55, self.car.fuel_amount)

if __name__ == '__main__':
    main()