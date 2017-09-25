class Room:
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
