class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age


    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
alvin = Person("alvin", 12)
kwaku = Person("Kwaku", 23)


print(alvin.get_age())