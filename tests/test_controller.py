import unittest
import os
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

    def test_add_staff_fails_if_wants_accommodation_is_true(self):
        num_people = len(self.dojo.added_people)
        self.assertFalse(self.dojo.add_person("Leo", "gets", "staff", "y"))
        self.assertEqual(len(self.dojo.added_people), num_people)

    def test_add_staff_person_is_successful_for_right_person_type(self):
        num_people = len(self.dojo.added_people)
        self.assertTrue(self.dojo.add_person("billy", "gates", "staff", "n"))
        self.assertEqual(len(self.dojo.added_people), num_people + 1)
        staff_person = self.dojo.added_people["Billy Gates"]
        self.assertTrue(staff_person)
        self.assertEqual(staff_person.name, "Billy Gates")
        self.assertEqual(staff_person.type_, "Staff")
        self.assertIsNone(staff_person.office_name)
        self.assertFalse(staff_person.is_allocated)

    def test_add_fellow_person_is_successful_for_right_person_type(self):
        num_people = len(self.dojo.added_people)
        self.assertTrue(self.dojo.add_person("billy", "gates", "fellow", "y"))
        self.assertEqual(len(self.dojo.added_people), num_people + 1)
        fellow = self.dojo.added_people["Billy Gates"]
        self.assertTrue(fellow)
        self.assertEqual(fellow.name, "Billy Gates")
        self.assertEqual(fellow.type_, "Fellow")
        self.assertIsNone(fellow.livingspace_name)
        self.assertIsNone(fellow.office_name)
        self.assertFalse(fellow.is_allocated)

    def test_print_room_fails_if_room_name_does_not_exist(self):
        self.assertFalse(self.dojo.print_room("red"))

    def test_print_room_passes_if_room_exists(self):
        num_rooms = len(self.dojo.all_created_rooms)
        self.assertTrue(self.dojo.create_room("office", ["blue"]))
        self.assertEqual(len(self.dojo.all_created_rooms), num_rooms + 1)
        self.assertTrue(self.dojo.print_room("blue"))

    def test_print_allocations_fails_if_no_rooms_are_created_yet(self):
        self.assertFalse(self.dojo.print_allocations())

    def test_print_allocations_passes_if_rooms_are_present(self):
        self.assertTrue(self.dojo.create_room("office", ["yellow", "red"]))
        self.assertTrue(self.dojo.print_allocations())

    def test_print_allocations_to_a_filename(self):
        self.assertTrue(self.dojo.create_room("office", ["yellow", "red"]))
        self.assertTrue(self.dojo.add_person("Leo", "gets", "staff", "n"))
        self.assertTrue(self.dojo.print_allocations("tests/files/allocated.txt"))
        self.assertTrue(os.path.exists("tests/files/allocated.txt"))

    def test_print_unallocated_fails_if_no_people_have_been_added_yet(self):
        self.assertFalse(self.dojo.print_unallocated())

    def test_print_unallocated_people_fails_when_all_people_have_been_allocated_rooms(self):
        self.assertTrue(self.dojo.create_room("office", ["blue"]))
        self.assertTrue(self.dojo.create_room("livingspace", ["kigali"]))
        self.assertTrue(self.dojo.add_person("bilbo", "gates", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("tai", "tai", "fellow", "y"))
        self.assertFalse(self.dojo.print_unallocated())

    def test_print_unallocated_if_no_rooms_have_been_created_yet(self):
        self.assertTrue(self.dojo.add_person("bilbo", "gates", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("tai", "tai", "fellow", "y"))
        self.assertFalse(self.dojo.print_unallocated())

    def test_print_unallocated_is_successful_for_added_people_without_rooms(self):
        self.assertTrue(self.dojo.create_room("office", ["blue"]))
        self.assertTrue(self.dojo.add_person("bilbo", "gates", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("tai", "tai", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("mama", "mzee", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("Augustus", "mwine", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("Brian", "mao", "staff", "n"))
        self.assertTrue(self.dojo.print_unallocated())

    def test_print_unallocated_writes_to_file(self):
        self.assertTrue(self.dojo.create_room("office", ["blue"]))
        self.assertTrue(self.dojo.add_person("bilbo", "gates", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("tai", "tai", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("mama", "mzee", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("Augustus", "mwine", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("Brian", "mao", "staff", "n"))
        self.assertTrue(self.dojo.print_unallocated("tests/files/unallocated.txt"))
        self.assertTrue(os.path.exists("tests/files/unallocated.txt"))

    def test_reallocate_person_fails_if_person_is_non_existent(self):
        self.assertTrue(self.dojo.create_room("office", ["blue"]))
        self.assertFalse(self.dojo.reallocate_person("Kibikindi Amos", "blue"))

    def test_reallocate_person_fails_when_room_with_that_name_is_non_existent(self):
        self.assertTrue(self.dojo.create_room("office", ["blue"]))
        self.assertTrue(self.dojo.add_person("kibikindi", "amos", "staff", "n"))
        self.assertFalse(self.dojo.reallocate_person("Kibikindi Amos", "blue"))

    def test_reallocate_staff_person_fails_for_livingspace_room_type(self):
        self.assertTrue(self.dojo.create_room("office", ["blue"]))
        self.assertTrue(self.dojo.create_room("livingspace", ["kigali"]))
        self.assertTrue(self.dojo.add_person("kibikindi", "amos", "staff", "n"))
        self.assertFalse(self.dojo.reallocate_person("kibikindi amos", "kigali"))

    def test_reallocate_person_fails_if_new_room_is_full(self):
        self.assertTrue(self.dojo.create_room("livingspace", ["kampala"]))
        self.assertTrue(self.dojo.add_person("bilbo", "gates", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("tai", "tai", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("mama", "mzee", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("augustus", "mwine", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("brian", "mao", "fellow", "y"))
        self.assertFalse(self.dojo.reallocate_person("brian mao", "kampala"))

    def test_reallocate_person_fails_for_a_person_who_never_wanted_accommodation(self):
        self.assertTrue(self.dojo.create_room("office", ["blue"]))
        self.assertTrue(self.dojo.add_person("bilbo", "gates", "fellow", "n"))
        self.assertTrue(self.dojo.create_room("livingspace", ["kampala"]))
        self.assertTrue(self.dojo.add_person("tai", "tai", "fellow", "y"))
        self.assertFalse(self.dojo.reallocate_person("bilbo gates", "kampala"))

    def test_reallocate_is_successful(self):
        self.assertTrue(self.dojo.add_person("mama", "mzee", "fellow", "y"))
        self.assertTrue(self.dojo.add_person("augustus", "mwine", "fellow", "y"))
        self.assertTrue(self.dojo.create_room("office", ["blue"]))
        self.assertTrue(self.dojo.reallocate_person("mama mzee", "blue"))
        self.assertTrue(self.dojo.create_room("livingspace", ["kampala"]))
        self.assertTrue(self.dojo.reallocate_person("mama mzee", "kampala"))

    def test_load_people_from_filename_fails_for_non_existent_filename(self):
        self.assertFalse(self.dojo.load_people("donal trump.txt"))

    def test_load_people_passes_for_given_filename(self):
        self.assertTrue(self.dojo.load_people("files/names.txt"))