import unittest
from app.controller import Dojo


class TestMainApp(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_create_room_fails_if_room_type_not_known(self):
        num_rooms = len(self.dojo.names_of_all_created_rooms)
        self.assertFalse(self.dojo.create_room("type", ["blue"]))
        self.assertEqual(len(self.dojo.names_of_all_created_rooms), num_rooms)