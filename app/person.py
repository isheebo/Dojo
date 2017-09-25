class Person:
    """Person represents a typical person within the Dojo"""

    def __init__(self, name):
        self.name = name.title()
        self.is_allocated = False
        self.office_name = None
        self.type_ = self.__class__.__name__


class Fellow(Person):
    def __init__(self, name, wants_accommodation=False):
        super(Fellow, self).__init__(name)
        self.wants_accommodation = wants_accommodation
        self.livingspace_name = None


class Staff(Person):
    def __init__(self, name):
        super(Staff, self).__init__(name)
