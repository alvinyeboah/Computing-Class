# Create a program that reads a duration from the user as a number of days, hours,
# minutes, and seconds. Compute and display the total number of seconds represented
# by this duration

s = int(input("Enter your number of seconds: "))
d = int(input("Enter your number of days: "))
h = int(input("Enter your number of hours: "))
m = int(input("Enter your number of minutes: "))

total = (60*m) +(60*60*h) + s + (60*60*24*d)

print(f"The total time in seconds is {total}")