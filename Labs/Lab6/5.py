def digitize(digits):
    dict1 = {}
    for x in digits:
        if x.isdigit():
            if x not in dict1:
                dict1[x] = 1
            else:
                dict1[x] += 1
    return dict1
print(digitize("1.24324"))