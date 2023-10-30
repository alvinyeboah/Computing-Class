# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume. Display the result rounded to one
# decimal place
import math

radius = int(input("WHat is the radius of your cylinder?: "))
height = int(input("WHat is the height of your cylinder?: "))
constant = math.pi

volume = round((constant * (radius**2) * height),1)

print(f"The volume of your cylinder is {volume}")
