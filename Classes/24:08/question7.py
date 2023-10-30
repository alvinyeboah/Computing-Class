# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.
# Hint: One foot is 12 inches. One inch is 2.54 centimeters.
# 3

feet= int(input("Enter your height(feet)"))
inches= int(input("Enter your height(inches)"))

rh = (inches*2.54) + (feet*12*2.54)

print(f"Your height in cm is {rh}")