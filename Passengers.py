from People import *


class Passengers(People):
    __list_passengers_flight = []

    def __init__(self, id, name, passport):
        super().__init__(id, name)
        self.__passport = passport
        self.__add_passenger_to_list()

    def __add_passenger_to_list(self):
        Passengers.__list_passengers_flight.append(self)

    @classmethod
    def get_list_object_passenger(cls):
        return cls.__list_passengers_flight