class Room:
    """ Base Model for a room within the Dojo"""
    def __init__(self, name):
        self.name = name.title()
        self.members = []
        self.max_capacity = 0
        self.type_ = self.__class__.__name__

    def is_empty(self):
        return len(self.members) == 0

    def is_full(self):
        return len(self.members) >= self.max_capacity

    def __repr__(self):
        template = "Room Name: \"{}\"  Type: \"{}\"\n------------------------------------------------------\n{}\n\n"
        return template.format(self.name, self.type_,
                               ", ".join([member.name for member in self.members]) if len(
                                   self.members) != 0 else "<-- No Members -->")


class Office(Room):
    """ Model for an Office within the Dojo"""
    def __init__(self, name):
        super(Office, self).__init__(name)
        self.max_capacity = 6
