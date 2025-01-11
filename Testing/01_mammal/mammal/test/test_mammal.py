from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal('Snake', 'Reptile', 'SSSS')

    def test_correct_init(self):

        self.assertEqual('Snake', self.mammal.name)
        self.assertEqual('Reptile', self.mammal.type)
        self.assertEqual('SSSS', self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_should_return_string(self):

        self.assertEqual("Snake makes SSSS", self.mammal.make_sound())

    def test_get_kingdom_return_kingdom(self):

        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info_should_return_string(self):

        self.assertEqual("Snake is of type Reptile", self.mammal.info())


if __name__ == '__main__':
    main()