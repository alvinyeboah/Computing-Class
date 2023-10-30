def dist(s,t):
    if len(s) == 0 :
        return len(t)
    elif  len(t)== 0:
        return len(s)
    else :
        cost = 0 
        if s[-1] != t[-1]:
            cost = 1
        d1 = dist(s[:-1],t) +1
        d2 = dist(s,t[:-1]) +1
        d3 = cost + dist(s[:-1],t[:-1])
        return min(d1,d2,d3)

result = dist("aaaaa","afaaa") 
print(result)       