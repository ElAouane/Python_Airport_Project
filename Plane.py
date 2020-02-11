from Aircraft import *


class Plane(Aircraft):
    __plane_lists = []

    def __init__(self, capacity, plane_serial, airline):
        super().__init__(capacity)
        self.plane_serial = plane_serial
        self.airline = airline
        self.plane_list = [capacity + ' ' + plane_serial + ' ' + airline]
        self.__add_plane_to_list()

    def show_plane(self):
        for plane in self.plane_list:
            print(plane)

    def __add_plane_to_list(self):
        Plane.__plane_lists.append(self)

    @classmethod
    def get_list_plane_objects(cls):
        return cls.__plane_lists
