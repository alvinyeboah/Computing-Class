new_list = []
l1= [40, 50, 10, 90]
l2 = [6, 2, 2, 5]
def pairwise_product(l1,l2):
    for x,y in zip(l1,l2):
        new_list.append(x*y)
    return new_list

print(pairwise_product(l1,l2))



