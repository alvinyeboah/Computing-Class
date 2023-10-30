def lower_uper_count(string):
    dict1 = {"lower" : 0, "upper" : 0}
    for x in string:
        if x.isupper():
            dict1["lower"] += 1
        elif x.islower() :
            dict1["upper"] += 1
    return dict1
print(lower_uper_count("aLVin"))