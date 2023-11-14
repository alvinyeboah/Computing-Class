l1= [40, 50, 10, 90]
l2= [60, 20, 19, 95]
new_list = []
def pairwise_ratio(l1,l2):
    for x,y in zip(l1,l2):
        new_list.append(round(x/y,3))
    return new_list
print(pairwise_ratio(l1,l2))