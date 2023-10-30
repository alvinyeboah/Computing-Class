def percentage_bump(old,new):
    value_increase= new-old
    percentage_increase = (value_increase/old) * 100
    print(f"{percentage_increase} ")

percentage_bump(62,133)