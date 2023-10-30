def averager():
    list = []
    sum = 0 
    while True:
        number = int(input("Enter your numbers to be averaged"))
        if number == 0:
            print(average)
            break
        else :  
            list.append(number)
            sum = sum + number
            average = sum/(len(list))

averager()        
