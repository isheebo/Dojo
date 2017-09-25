class Person:
    """Person represents a typical person within the Dojo"""

    def __init__(self, name):
        self.name = name.title()
        self.is_allocated = False
        self.office_name = None
        self.type_ = self.__class__.__name__
