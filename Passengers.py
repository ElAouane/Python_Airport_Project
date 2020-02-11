from People import *
from Flight import *

list = []
class Passengers(People):
    def __init__(self, id, name, passport):
        super().__init__(id, name)
        self.__passport = passport
        self.available_pass = [id, name, passport]


    def show_passengers(self):
        for passenger in self.available_pass:
            print(passenger)



