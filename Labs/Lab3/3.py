first_side = int(input("Enter the length of your first side: "))
second_side = int(input("Enter the length of your second side: "))
third_side = int(input("Enter the length of your third side: "))

if first_side == second_side and second_side == third_side:
    print(f"Your triangle is equilateral")
elif first_side ==  second_side and second_side != third_side:
    print(f"Your triangle is isosceles") 
else:
    print(f"Your triangle is scalene")     