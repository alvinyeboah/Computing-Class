score = int(input("what's your percentage score?"))

if score >= 85 and score<101 :
    print(f"Your grade is an A+")
elif score >=80 and score <85 :
    print(f"Your grade is an A")   
elif score >=75 and score <80 :
    print(f"Your grade is an B+")   
elif score >=70 and score <75 :
    print(f"Your grade is an B")   
elif score >=65 and score <70 :
    print(f"Your grade is an C+")   
elif score >=60 and score <65 :
    print(f"Your grade is an C")   
elif score >=55 and score <60 :
    print(f"Your grade is an D")   
elif score >=50 and score <55 :
    print(f"Your grade is an D")   
elif score <50 :
    print(f"Your grade is an E")      
elif score >100 :
    print(f"Your grade is incorrect")                                