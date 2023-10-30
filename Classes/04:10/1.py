def total_values():
    user_input = input("Enter your number")
    if user_input == "":
        return 0.0 
    else :
        return float(user_input) + total_values()
print(total_values())