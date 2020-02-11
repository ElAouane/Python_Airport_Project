from Passengers import *


class Flight:

    __list_flights = []

    def __init__(self, flight_number, origin, destination, datetime):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.datetime = datetime
        self.__add_flight_to_list()


    def show_available_flight(self):
        for item in self.available_flight:
            print(item)

    def __add_flight_to_list(self):
        Flight.__list_flights.append(self)


    # method to append a customer

    # Class methods //
    @classmethod
    def get_list_objsct(cls):
        return cls.__list_flights




