def unique_characters(word):
    mydict = {}
    for x in word:
        if x in mydict:
            mydict[x] += 1
        else:
            mydict[x] = 1
    for key, value in list(mydict.items()):
        if value != 1:
            del mydict[key]
    return len(mydict)

result = unique_characters("zzzjvcd")
print(result)