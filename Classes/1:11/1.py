import random

def simulate_diceroll():
    first_roll = random.randrange(1, 7)
    second_roll = random.randrange(1, 7)
    total = first_roll + second_roll
    return total

def main():
    my_dict = {}
    for _ in range(1000):
        total = simulate_diceroll()

        if total not in my_dict:
            my_dict[total] = 1
        else:
            my_dict[total] += 1

    display_summary(my_dict)

def display_summary(sample_dictionary):
    print("{:<8} {:<20} {:<20}".format("Total", "Simulated Percent", "Expected Percent"))
    for total, frequency in sample_dictionary.items():
        print("{:<8} {:<20} {:<20}".format(total, round((frequency / 1000) * 100, 2), round((frequency / 11) * 100, 2)))


main()