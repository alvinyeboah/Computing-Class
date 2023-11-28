class Annmarie:
    def __init__(self, name, age, school):
      self.name = name
      self.age = age
      self.school = school


    def change_name(self,new_name):
        self.name = new_name

person1 = Annmarie("ann",12,"ashesi")

print(person1.name)