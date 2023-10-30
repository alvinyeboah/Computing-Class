# pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added to the
# balance of the savings account. Write a program that begins by reading the amount of
# money deposited into the account from the user. Then your program should compute
# and display the amount in the savings account after 1, 2, and 3 years. Display each
# amount so that it is rounded to 2 decimal places.
# For example, if the initial deposit by the user is 50,000 Ghana cedis, the interest earned
# after 1 year is (4/100) x (50000). This amount is added to 50,000 to represent the
# amount in the savings account after 1 year. The process is then repeated to find the
# amount in the savings account after 2 years, and then after 3 years


amnt = int(input("Enter amount deposited into account: "))
rate = 0.04  

for y in range(4):
    new_amnt = amnt * (1 + rate)**y
    print(f"The total amount after {y} years is {new_amnt}")
    