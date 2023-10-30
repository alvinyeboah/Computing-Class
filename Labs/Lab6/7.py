def anagrams(string1,string2):
    dictionary1= dict()
    dictionary2= dict()
    for x in string1:
        if x in dictionary1:
            dictionary1[x] += 1
        else :
            dictionary1[x] = 1
    for x in string2:
        if x in dictionary2:
            dictionary2[x] += 1
        else :
            dictionary2[x] = 1
    return dictionary1 == dictionary2
print(anagrams("alvin","nivla"))
