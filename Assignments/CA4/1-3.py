new_list = []
l1 = [40, 50, 10, 90, 100, 70]
l2 = [60, 20, 19, 95, 30, 20]

def smaller_indices(l1, l2):
    for index, (x, y) in enumerate(zip(l1, l2)):
        if x < y:
            new_list.append(index)
    return new_list

print(smaller_indices(l1, l2))