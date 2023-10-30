x =int(input("Enter your number:"))
guess = x/2
condition = abs((guess * guess - x))
while True :
    avg = (guess + ((x/guess)))/2
    not_good = abs(guess * guess - x)

    if not_good <=10**-12:
        break
    guess = avg  
print(guess)    
