import unittest
from app.person import Person, Fellow, Staff


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("Billy Baggins")

    def test_person_is_created(self):
        self.assertTrue(Person)
        self.assertEqual(self.person.name, "Billy Baggins")
        self.assertFalse(self.person.is_allocated)
        self.assertIsNone(self.person.office_name)
        self.assertEqual(self.person.type_, "Person")


class TestFellow(unittest.TestCase):
    def setUp(self):
        self.fellow = Fellow("billy baggins")

    def test_fellow_is_created(self):
        self.assertEqual(self.fellow.name, "Billy Baggins")
        self.assertEqual(self.fellow.type_, "Fellow")
        self.assertIsNone(self.fellow.office_name)
        self.assertIsNone(self.fellow.livingspace_name)
        self.assertFalse(self.fellow.is_allocated)


class TestStaff(unittest.TestCase):
    def setUp(self):
        self.staff = Staff("Billy baggins")

    def test_staff_is_created(self):
        self.assertEqual(self.staff.name, "Billy Baggins")
        self.assertFalse(self.staff.is_allocated)
        self.assertIsNone(self.staff.office_name)
        self.assertEqual(self.staff.type_, "Staff")
