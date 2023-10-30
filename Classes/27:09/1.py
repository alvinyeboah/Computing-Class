day = int(input("Enter yourtime in days"))
hours= int(input("Enter yourtime in hours"))
minutes= int(input("Enter yourtime in minutes"))
seconds = int(input("Enter yourtime in seconds "))

sum = (day * 86400) + (minutes * 60) +seconds + (hours * 60 * 60)
print(sum)
