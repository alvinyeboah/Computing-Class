from person import Person

class Car:
    def __init__(self, make, model, year, license_plate):
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.driver = None
        self.front_passenger = None
        self.back_passenger1 = None
        self.back_passenger2 = None
        self.back_passenger3 = None

    def __str__(self):
        return f"Car: {self.year} {self.make} {self.model}, License Plate: {self.license_plate}"

    def set_driver(self, person):
        if person.allowed_to_drive():
            self.driver = person
            return True
        else:
            return False

    def has_driver(self):
        return self.driver is not None

    def add_passenger(self, person):
        if person.age < 10 and person is self.front_passenger:
            return False  

        if self.front_passenger is None:
            self.front_passenger = person
        elif self.back_passenger1 is None:
            self.back_passenger1 = person
        elif self.back_passenger2 is None:
            self.back_passenger2 = person
        elif self.back_passenger3 is None:
            self.back_passenger3 = person
        else:
            return False 
        return True

    def has_passengers(self):
        if self.front_passenger is not None:
            return True
        if self.back_passenger1 is not None:
            return True
        if self.back_passenger2 is not None:
            return True
        if self.back_passenger3 is not None:
            return True
        return False

    def get_num_occupants(self):
        count = 1  
        if self.front_passenger is not None:
            count += 1
        if self.back_passenger1 is not None:
            count += 1
        if self.back_passenger2 is not None:
            count += 1
        if self.back_passenger3 is not None:
            count += 1
        return count

    def get_num_passengers(self):
        count = 0
        if self.front_passenger is not None:
            count += 1
        if self.back_passenger1 is not None:
            count += 1
        if self.back_passenger2 is not None:
            count += 1
        if self.back_passenger3 is not None:
            count += 1
        return count

    def is_empty(self):
        return not self.has_driver() and not self.has_passengers()

    def is_full(self):
        return all(passenger is not None for passenger in [self.driver, self.front_passenger, self.back_passenger1, self.back_passenger2, self.back_passenger3])

    def list_riders(self):
        print(f"Driver: {self.driver.name} ({self.driver.age} years old)")
        if self.front_passenger is not None:
            print(f"Front Passenger: {self.front_passenger.name} ({self.front_passenger.age} years old)")
        if self.back_passenger1 is not None:
            print(f"Back Passenger 1: {self.back_passenger1.name} ({self.back_passenger1.age} years old)")
        if self.back_passenger2 is not None:
            print(f"Back Passenger 2: {self.back_passenger2.name} ({self.back_passenger2.age} years old)")
        if self.back_passenger3 is not None:
            print(f"Back Passenger 3: {self.back_passenger3.name} ({self.back_passenger3.age} years old)")

if __name__ == "__main__":
    person1 = Person("Ayorkor", 23)
    person2 = Person("Chudah", 17)
    person3 = Person("Kwame", 8)

    # testing Car class
    car = Car("Toyota", "Camry", 2022, "ABC123")


    print("Setting driver:")
    print("Success:", car.set_driver(person1))  
    print("Success:", car.set_driver(person2))  

    # Testing has_driver method
    print("\nChecking if car has a driver:")
    print("Has driver:", car.has_driver())  

    # Testing add_passenger method
    print("\nAdding passengers:")
    print("Success:", car.add_passenger(person3)) 
    print("Success:", car.add_passenger(person2)) 
    print("Success:", car.add_passenger(person1)) 
    print("Success:", car.add_passenger(person1))  

    # Testing has_passengers method
    print("\nChecking if car has passengers:")
    print("Has passengers:", car.has_passengers())  

    # Testing get_num_occupants method
    print("\nGetting number of occupants in the car:")
    print("Number of occupants:", car.get_num_occupants())  

    # Testing get_num_passengers method
    print("\nGetting number of passengers in the car:")
    print("Number of passengers:", car.get_num_passengers()) 

    # Testing is_empty method
    print("\nChecking if the car is empty:")
    print("Is empty:", car.is_empty())  

    # Testing is_full method
    print("\nChecking if the car is full:")
    print("Is full:", car.is_full())  

    # Testing list_riders method
    print("\nListing riders in the car:")
    car.list_riders()
