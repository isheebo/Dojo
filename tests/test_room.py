import unittest
from app.room import Room, Office, LivingSpace


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("nairobi")

    def test_room_is_created(self):
        self.assertEqual(self.room.name, "Nairobi")
        self.assertEqual(self.room.max_capacity, 0)
        self.assertEqual(self.room.members, [])
        self.assertTrue(self.room.is_empty())
        self.assertEqual(self.room.type_, "Room")


class TestOffice(unittest.TestCase):
    def setUp(self):
        self.office = Office("blue")

    def test_office_created(self):
        self.assertEqual(self.office.name, "Blue")
        self.assertEqual(self.office.max_capacity, 6)
        self.assertEqual(self.office.members, [])
        self.assertEqual(self.office.type_, "Office")
        self.assertTrue(self.office.is_empty())
