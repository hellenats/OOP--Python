from unittest import TestCase, main
# from cat import Cat


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat('Pissy')

    def test_correct_init(self):

        self.assertEqual('Pissy', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_when_cat_is_fed_raises_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_eat_when_cat_is_not_fed_makes_cat_fed_and_sleepy_and_increases_size(self):

        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_sleep_when_not_fed_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertFalse(self.cat.fed)
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


    def test_sleep_when_cat_is_fed_makes_cat_not_sleepy(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertTrue(self.cat.fed)
        self.assertFalse(self.cat.sleepy)



if __name__ == '__main__':
    main()