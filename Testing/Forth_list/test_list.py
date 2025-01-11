from unittest import TestCase, main

# from Forth_list.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.int_list = IntegerList(8.8, 1, 2, 3, 'hello')

    def test_correct_init(self):

        self.assertEqual([1, 2, 3], self.int_list.get_data())

    def test_add_with_non_integer_value_raises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.int_list.add('eho')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_with_integer_value_appends_the_new_value(self):

        expected_list = self.int_list.get_data().copy() + [8]

        self.int_list.add(8)

        self.assertEqual(expected_list, self.int_list.get_data())

    def test_remove_index_with_out_of_range_index_should_raise_index_error(self):

        with self.assertRaises(IndexError) as ie:
            self.int_list.remove_index(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_with_valid_index_should_remove_the_element_on_index(self):

        self.int_list.remove_index(1)

        self.assertEqual([1, 3], self.int_list.get_data())

    def test_get_with_out_of_range_index_should_raise_index_error(self):

        with self.assertRaises(IndexError) as ie:
            self.int_list.get(10)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_valid_index_should_return_the_element(self):

        result = self.int_list.get(0)

        self.assertEqual(1, result)
        self.assertEqual([1, 2, 3], self.int_list.get_data())

    def test_insert_with_out_of_range_index_should_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.insert(10, 5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_with_valid_index_but_non_integer_value_raises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.int_list.insert(1, 5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_with_valid_index_and_integer_value_should_insert_new_element_on_position(self):

        expected_int_list = self.int_list.get_data().copy()
        expected_int_list.insert(1, 5)

        self.int_list.insert(1, 5)

        self.assertEqual(expected_int_list, self.int_list.get_data())

    def test_get_biggest_should_return_biggest_number(self):

        result = self.int_list.get_biggest()

        self.assertEqual(3, result)

    def test_get_index_returns_the_index_of_element(self):

        element = self.int_list.get_index(3)

        self.assertEqual(2, element)


if __name__ == "__main__":
    main()
