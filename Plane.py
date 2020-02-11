from Aircraft import *

class Plane(Aircraft):
    def __init__(self, capacity, plane_serial, airline):
        super().__init__(capacity)
        self.plane_serial = plane_serial
        self.airline = airline
        self.plane_list = [capacity + ' ' + plane_serial + ' ' + airline]

    def show_plane(self):
        for plane in self.plane_list:
            print(plane)



