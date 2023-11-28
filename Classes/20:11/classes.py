''' 
Functions in a class are called methods
the constructor function is the first function in the class
'''

class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age  
        


    person1 = Person("alvin", 12)
    person2 = Person("yaw", 34)



class Car:
    def __init__(self, make, brand, year, color):
        self.make = make
        self.brand = brand
        self.year = year
        self.color = color

    def change_make(self, new_make):
        self.make = new_make

    def allowed_to_drive(self):
        if self.year <=2012:
            return True
        else:
            return False
    
if __name__ == "__main__":
    car1 = Car("Camry", "Toyota", 2022, "red")

    car1.change_make("Corolla")
    drive_result  = car1.allowed_to_drive()
    print(drive_result)


