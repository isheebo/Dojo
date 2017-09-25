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
