year = int(input("Enter your year: "))

if year % 400 ==0:
    print(f"Your year {year} is a leap year.")
elif year % 100 ==0 :
    print(f"Your year {year} is not a leap year.")
elif year % 4 ==0:
        print(f"Your year {year} is a leap year.")
else :
        print(f"Your year {year} is not a leap year.")
    
