# __AIRPORT_FLIGHT_ASSISTANT__
## **Airport:**
* Create the classes required for a full functionality of the project. The Classes consists in
    - `People.py` : Create a basic class with basic parameters and from which to inehrit to create other subclasses.
    - `Passengers.py` : Inherit from Parent class and add parameters to make passeners unique
    - `Flight.py` : A class to set a list of flights available in the airport and for the Passengers
    - `Aicraft.py` : Set a class to define `plane` details
    - `Checking_Assistant.py` : `Main()` Entry point of the program where method classes are called
* The basic functionality of the program is to be able to build step by step a intire functional airport based on the class object orientations.
* The classes in  each `.py` are build to inherit from each other or to import some functionality from another class so the program can offer different choice to the Flight Assistant.

## **Blockers, Problems, Bugs, Solutions:**
* __Blockers:__ Had Problem to Manage a 'MVC' model, where to separate Model and Control in classes file, while keep the View only in Checking Assistant. The main problem is to understand how to create and initiate a class with all parameters in a list
* __Problems:__ The program, seems to be able to set a list for me, but unable to loop through it.
* __Bugs:__ N/A
* __Solutions:__
    * __Problems:__ The main problem was to print properly my lists in the console, i just realised that i was passing the wrong syntac in the list, so instead of printing the data in 1 line, was printing on single lines, making the output confusing.
    * __Bugs:__


## **Outcomes:**
