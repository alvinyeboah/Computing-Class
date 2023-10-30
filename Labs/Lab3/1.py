import math

first_num = int(input("Enter your first number: "))
second_num = int(input("Enter your second number: "))
third_num = int(input("Enter your third number: "))

initial_list= []
initial_list.append(first_num)
initial_list.append(second_num)
initial_list.append(third_num)

mid = int((math.ceil(len(initial_list))/2))

final_list= []
final_list.append(min(initial_list))
final_list.append(initial_list[mid])
final_list.append(max(initial_list))
print(final_list)