ta=int(input("Enter your current air temperature in degree celsius:"))
V=int(input("Enter your current wind speed in kilometres:"))

WCI = round(13.12+ (0.6215*ta) - (11.37*(V**0.16)) +(0.3965*ta*(V**0.16)))

print(f"Your wind chill index is {WCI} ")
