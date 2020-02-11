from Aircraft import *
from Flight import *
from Passengers import *
from Plane import *
from Flight import *


def main():
    passenger1 = Passengers('1', 'David', 'BG2365215')
    passenger2 = Passengers('2', 'Dave', 'BG256398')
    passenger3 = Passengers('3', 'John', 'BG236589')
    passenger4 = Passengers('4', 'Susan', 'HG5236598')
    passenger5 = Passengers('5', 'Carol', 'BG2541896')
    passenger6 = Passengers('6', 'Karen', 'BG2563985')

    plane1 = Plane('300', '3265841', 'EasyJet')
    plane2 = Plane('600', '3265895', 'Alitalia')
    plane3 = Plane('700', '124578', 'Hamza')
    flight1 = Flight('215487', 'UK', 'Italy', '12.00')
    flight2 = Flight('256369', 'IT', 'UK', '12.00')
    flight3 = Flight('215487', 'SPAIN', 'MOROCCO', '12.00')

    done = False
    while done == False:
        print("""======AIRPORT MANAGEMENT======
        1. Display all the passengers
        2. Display Aircrafts
        3. Display Flight List
        """)
        choice = int(input("Enter Choice: "))
        if choice == 1:
            for passenger in Passengers.get_list_object_passenger():
                print(passenger.id + ' ' + passenger.name + ' ' + passenger._Passengers__passport)
        if choice == 2:
            for planes in Plane.get_list_plane_objects():
                print(planes.capacity + ' ' + planes.plane_serial + ' ' + planes.airline)
        if choice == 3:
            #print(Flight.get_list_objsct())
            for flights in Flight.get_list_objsct():
                print(flights.flight_number + ' ' + flights.origin + ' ' + flights.destination + ' ' + flights.datetime)


main()
