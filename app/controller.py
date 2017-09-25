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
