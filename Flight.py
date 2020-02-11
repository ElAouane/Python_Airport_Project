from Passengers import *


class Flight:
    def __init__(self, flight_number, origin, destination, datetime):
        # self.flight_number = flight_number
        # self.origin = origin
        # self.destination = destination
        # self.datetime = datetime
        self.available_flight = [flight_number, origin, destination, datetime]

    def show_available_flight(self):
        for item in self.available_flight:
            print(item)




