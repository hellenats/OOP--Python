from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student('Test')
        self.student_with_courses = Student('Test2', {'math': ["1 + 1 = 2"]})

    def test_correct_init(self):
        self.assertEqual('Test', self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({'math': ["1 + 1 = 2"]}, self.student_with_courses.courses)

    def test_enroll_with_existing_course_append_new_notes(self):
        expected_update_of_course_notes = ["1 + 1 = 2", "x * y = xy", "a + b = (a + b)"]

        expected_message = self.student_with_courses.enroll(
            'math',
            ["x * y = xy", "a + b = (a + b)"])

        self.assertEqual(expected_update_of_course_notes, self.student_with_courses.courses['math'])
        self.assertEqual("Course already added. Notes have been updated.", expected_message)

    def test_enroll_with_new_course_and_Y_as_third_param_adds_the_course_and_notes(self):
        expected_courses = {'literature': ['Ana Huang', 'J.K.Rowling']}

        expected_message = self.student.enroll(
            'literature',
            ['Ana Huang', 'J.K.Rowling'],
            'Y')

        self.assertEqual(expected_courses, self.student.courses)
        self.assertEqual("Course and course notes have been added.", expected_message)

    def test_enroll_with_new_course_and_empty_string_as_third_param_adds_the_course_and_notes(self):
        expected_courses = {'literature': ['Ana Huang', 'J.K.Rowling']}

        expected_message = self.student.enroll(
            'literature',
            ['Ana Huang', 'J.K.Rowling'],
            '')

        self.assertEqual(expected_courses, self.student.courses)
        self.assertEqual("Course and course notes have been added.", expected_message)

    def test_enroll_with_new_course_and_NO_as_third_param_should_not_append_notes(self):
        expected_courses = {'math': []}

        expected_message = self.student.enroll(
            'math',
            ["x * y = xy", "a + b = (a + b)"],
            'NO')

        self.assertEqual("Course has been added.", expected_message)
        self.assertEqual(expected_courses, self.student.courses)

    def test_add_notes_to_existing_course(self):
        expected_update_of_course_notes = ["1 + 1 = 2", "x * y = xy"]

        expected_message = self.student_with_courses.add_notes(
            'math',
            "x * y = xy")

        self.assertEqual(expected_update_of_course_notes, self.student_with_courses.courses['math'])
        self.assertEqual("Notes have been updated", expected_message)

    def test_add_notes_to_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('math', 'a + b = (a + b)')

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_when_existing_removes_course(self):
        expected_message = self.student_with_courses.leave_course('math')

        self.assertEqual("Course has been removed", expected_message)
        self.assertEqual({}, self.student_with_courses.courses)

    def test_leave_course_which_does_not_exists_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('math')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == '__main__':
    main()