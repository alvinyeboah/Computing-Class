l1 = [1,2,3,4,4,5,33,67,8,9,0,-6]
def  min_index(nums):
    index = -1
    x =max(nums)
    for y in l1:
        index +=1
        if y == x :
            return index
print(min_index(l1))