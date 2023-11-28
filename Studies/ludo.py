import random as r

total1 = 62
total2 = 62
enterstate1 = False
enterstate2 = False

while True:
    played = input("Enter player key: ")

    if played == "r1":
        rand1 = r.randint(1, 6)
        print(f"You played a {rand1}.")
        if rand1 == 6:
            enterstate1 = True
            print("You have entered the game.")
        else:
            print("Play again to move.")
    if enterstate1:
            total1 -= rand1

    elif played == "r2":
        rand2 = r.randint(1, 6)
        print(f"You played a {rand2}.")
        if rand2 == 6:
            enterstate2 = True
            print("You have entered the game.")
        else:
            print("Play again to move.")
        if enterstate2:
            total2 -= rand2
    if total1 ==56:
        print(f"Total for player 1: {total1}")
    if total2 ==56:
        print(f"Total for player 2: {total2}")
