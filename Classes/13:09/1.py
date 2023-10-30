def euclid(a,b):
    if b == 0:
        return a
    else:
        c = a % b
        return euclid(b,c)
result = euclid(100,235)
print(result)
