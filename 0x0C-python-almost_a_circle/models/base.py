#!/usr/bin/python3



class Base:
    """Base class body.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Id in a constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
