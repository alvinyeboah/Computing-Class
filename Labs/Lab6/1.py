def prog(string):
    dict1 = {}
    for x in string:
        if x in dict1:
            dict1[x] += 1
        else:
            dict1[x] = 1
    for key,values in dict1.items():
        print(key, values) 

prog("alvin")    