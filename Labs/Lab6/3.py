def OddEvenCOunt(integers):
    numdict={"even" : 0 , "odd" : 0}
    for x in integers:
        if x % 2 == 0 :
            numdict["even"] +=1
        else:
            numdict["odd"] += 1

    return numdict

print(OddEvenCOunt([1,2,3,4,45,6,6]))
