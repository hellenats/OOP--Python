from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(100, 150)

    def test_correct_init_(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(150, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_with_not_enough_fuel_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10_000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_should_decrease_fuel(self):
        self.vehicle.drive(10)

        self.assertEqual(87.5, self.vehicle.fuel)

    def test_refuel_with_when_capacity_is_full_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_fuel_just_enough_to_fill_capacity(self):
        self.vehicle.fuel = 90
        self.vehicle.refuel(10)
        self.assertEqual(100, self.vehicle.fuel)

    def test_str_should_return_correct_string(self):
        self.assertEqual("The vehicle has 150 horse power with 100 fuel left and"
                         " 1.25 fuel consumption", self.vehicle.__str__())


if __name__ == "__main__":
    main()