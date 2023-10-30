frequency = int(input("What is your frequency: "))

if frequency < 3*10^9:
    print("These are radio waves")
elif frequency >= 3*10^9 and frequency <3*10^12:
    print("These are Microwaves")   
elif frequency >= 3*10^12 and frequency <4.3*10^14:
    print("This is Infrared Light") 
elif frequency >= 4.3*10^14 and frequency <7.5*10^14:
    print("This is visible light") 
elif frequency >= 7.5*10^14 and frequency <3*10^17:
    print("This is UV light") 
elif frequency >= 3*10^17 and frequency <3*10^19:
    print("These are X-rays") 
elif frequency >3*10^19:
    print("These are gamma rays")                     