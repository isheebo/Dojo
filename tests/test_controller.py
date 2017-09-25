import unittest
from app.controller import Dojo


class TestMainApp(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_create_room_fails_if_room_type_not_known(self):
        num_rooms = len(self.dojo.names_of_all_created_rooms)
        self.assertFalse(self.dojo.create_room("type", ["blue"]))
        self.assertEqual(len(self.dojo.names_of_all_created_rooms), num_rooms)

    def test_create_room_fails_if_room_name_already_exists(self):
        num_rooms = len(self.dojo.names_of_all_created_rooms)
        self.assertTrue(self.dojo.create_room("office", ["blue"]))
        self.assertEqual(len(self.dojo.names_of_all_created_rooms), num_rooms + 1)
        self.assertFalse(self.dojo.create_room("livingspace", ["blue"]))
        self.assertEqual(len(self.dojo.names_of_all_created_rooms), num_rooms + 1)

    def test_create_room_passes_for_single_room_input(self):
        num_rooms = len(self.dojo.names_of_all_created_rooms)
        self.assertTrue(self.dojo.create_room("office", ["blue"]))
        self.assertEqual(len(self.dojo.names_of_all_created_rooms), num_rooms + 1)
        self.assertTrue(self.dojo.create_room("livingspace", ["kigali"]))
        self.assertEqual(len(self.dojo.names_of_all_created_rooms), num_rooms + 2)

    def test_create_room_fails_for_multiple_rooms_if_type_unknown(self):
        num_rooms = len(self.dojo.names_of_all_created_rooms)
        self.assertFalse(self.dojo.create_room("type", ["blue", "orange", "yellow"]))
        self.assertEqual(len(self.dojo.names_of_all_created_rooms), num_rooms)

    def test_create_room_fails_for_multiple_rooms_if_one_of_room_names_exists(self):
        num_rooms = len(self.dojo.names_of_all_created_rooms)
        self.assertTrue(self.dojo.create_room("office", ["blue", "yellow", "orange"]))
        self.assertEqual(len(self.dojo.names_of_all_created_rooms), num_rooms + 3)
        self.assertFalse(self.dojo.create_room("office", ["green", "fuchsia", "yellow"]))
        self.assertEqual(len(self.dojo.names_of_all_created_rooms), num_rooms + 3)

    def test_create_room_passes_for_right_type_and_room_name(self):
        num_rooms = len(self.dojo.names_of_all_created_rooms)
        self.assertTrue(self.dojo.create_room("livingspace", ["kigali", "nairobi"]))
        self.assertEqual(len(self.dojo.names_of_all_created_rooms), num_rooms + 2)
        self.assertTrue(self.dojo.create_room("office", ["blue", "yellow", "red"]))
        self.assertEqual(len(self.dojo.names_of_all_created_rooms), num_rooms + 5)

    def test_add_person_fails_for_incorrect_person_type(self):
        num_people = len(self.dojo.added_people)
        self.assertFalse(self.dojo.add_person("billy", "gates", "person_type", "n"))
        self.assertEqual(len(self.dojo.added_people), num_people)

    def test_add_person_fails_if_name_already_exists(self):
        num_people = len(self.dojo.added_people)
        self.assertTrue(self.dojo.add_person("billy", "gates", "staff", "n"))
        self.assertEqual(len(self.dojo.added_people), num_people + 1)
        self.assertFalse(self.dojo.add_person("billy", "gates", "staff", "n"))
        self.assertEqual(len(self.dojo.added_people), num_people + 1)
        self.assertFalse(self.dojo.add_person("billy", "gates", "fellow", "y"))
        self.assertEqual(len(self.dojo.added_people), num_people + 1)
