pi = "3.1415926535897932384626433832795028841971693993751"
def digitize(digits):
    dict1 = {}
    for x in pi:
        if x not in dict1:
            dict1[x] = 1
        else:
            dict1[x] += 1
    return dict1
print(digitize(pi))