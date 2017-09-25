import random
from termcolor import cprint
from app.room import LivingSpace, Office
from app.person import Staff, Fellow


class Dojo:
    """Dojo: controls the allocation of rooms and admission of people into the Dojo"""

    def __init__(self):
        self.names_of_all_created_rooms = []
        self.all_created_rooms = dict()
        self.names_of_all_added_people = []
        self.added_people = dict()

    def create_room(self, room_type, room_names):
        """ Given a room type, create_room creates a room with
        the given name for a room_name specified in room_names
        @:param room_type: string
        @:param room_names: list
        @:returns True when room creation is successful False otherwise
        """

        valid_room_names = []
        room_type = room_type.lower()
        if room_type not in ("livingspace", "office"):
            cprint("unknown room type: rooms can be of either "
                   "livingspace or office types.", color="red")
            return False

        for room_name in room_names:
            room_name = room_name.title()
            if room_name in self.names_of_all_created_rooms:
                cprint(f"a room with name '{room_name}' already exists: please use a different name",
                       color="red")
                return False
            if room_name:
                valid_room_names.append(room_name)

        for room_name in valid_room_names:
            self.__create(room_type, room_name)
        return True

    def __create(self, room_type, room_name):
        """ helper function for create_room """
        if room_type == "office":
            new_room = Office(room_name)
            cprint(f"An office called {room_name} has been successfully"
                   " created!", color="green")

            self.all_created_rooms[new_room.name] = new_room
            self.names_of_all_created_rooms.append(new_room.name)
            return True
        new_room = LivingSpace(room_name)
        cprint(f"A livingspace called {room_name} has been successfully"
               " created!", color="green")

        self.all_created_rooms[new_room.name] = new_room
        self.names_of_all_created_rooms.append(new_room.name)
        return True

    def add_person(self, first_name, last_name, person_type, wants_accommodation):
        """ add_person adds a person to the Dojo. If rooms are available,
        it allocates the person a room according to their type"""
        person_type = person_type.lower()
        if person_type not in ("fellow", "staff"):
            cprint("unknown person type: persons can be of either fellow or staff type")
            return False

        name = f"{first_name} {last_name}"

        if name.title() in self.names_of_all_added_people:
            cprint("person already exists: can't add them twice", color="red")
            return False

        wants_accommodation = True if wants_accommodation and wants_accommodation.lower() in ("yes", "y") else False

        if wants_accommodation and person_type == "staff":
            cprint("staff members cannot be accommodated at the Dojo's livingspaces", color="red")
            return False

        is_added = False

        if person_type == "staff":
            person = Staff(name)
            cprint(f"{person.name} has been added successfully", color="blue")
            self.added_people[person.name] = person
            is_added = True
            self.names_of_all_added_people.append(person.name)
            if len(self.available_offices()) != 0:
                office = random.choice(self.available_offices())
                cprint(f"{first_name.title()} has been allocated office {office.name}", color="green")
                office.members.append(person)
                person.office_name = office.name
                person.is_allocated = True
            else:
                cprint(f"{first_name.title()} has not been allocated an office yet", color="yellow")

        if person_type == "fellow":
            person = Fellow(name, wants_accommodation)
            is_added = True
            self.added_people[person.name] = person
            self.names_of_all_added_people.append(person.name)
            cprint(f"{person.name} has been added successfully", color="blue")
            if len(self.available_offices()) != 0:
                office = random.choice(self.available_offices())
                cprint(f"{first_name.title()} has been allocated office {office.name}", color="green")
                office.members.append(person)
                person.office_name = office.name
                person.is_allocated = True if not wants_accommodation else False
            else:
                cprint(f"{first_name.title()} has not been allocated an office yet", color="yellow")

            if wants_accommodation:
                if len(self.available_livingspaces()) != 0:
                    livingspace = random.choice(self.available_livingspaces())
                    cprint(f"{first_name.title()} has been allocated livingspace {livingspace.name}", color="blue")
                    livingspace.members.append(person)
                    person.livingspace_name = livingspace.name
                    person.is_allocated = True if person.office_name and person.livingspace_name else False
                else:
                    cprint(f"{person.name} has not been allocated a living space as yet! create some rooms to add them",
                           color="yellow")
        return is_added

    def available_offices(self):
        """checks for office rooms. if they are available, returns a list of empty offices"""
        available_offices = []
        for room in self.all_created_rooms.values():
            if room.type_ == "Office" and not room.is_full():
                available_offices.append(room)
        return available_offices
