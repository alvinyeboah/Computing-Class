import math

def mysqrt(a,x):

    while True:
        y = (x + a/x) / 2
        if y == x:
            return x 
            break
        x= y
       



def test_square_root():
    print(f"a my_sqrt(a) math.sqrt(a) diff  ")
    diff = math.sqrt(2) - mysqrt(2,4)
    print(f"a {mysqrt(2,4)} {math.sqrt(2)} {diff}")

test_square_root()