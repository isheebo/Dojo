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
