texts = int(input("Enter the number of texts you sent: "))
airtime = int(input("Enter the time you spent on calls : "))

if texts <=50 and airtime <=50:
    total= round((15.44 + (15.44)*0.05),2)
    sales_tax= 0.05*(15+0.44)
    print(f"Your incurred a cost of ${total} without any extra charges.\n Your sales tax was {sales_tax} and your 911 call charge was $0.44 ")
elif texts >50 and airtime <=50:
    extra_charges = 0.15*(texts-50)
    total = (extra_charges + 0.44 + 15)
    sales_tax= round(total*0.05,2)
    final = round((total+ sales_tax),2)
    print(f"Your incurred a cost of ${final} with extra charges of {round(extra_charges,2)} for {texts-50} extra texts. \n Your sales tax was {sales_tax} and your 911 call charge was $0.44 ")
elif airtime >50 and text <=50:
    extra_charges = 0.25*(airtime-50)
    total = (extra_charges + 0.44 + 15)
    sales_tax= round(total*0.05,2)
    final = round((total+ (total * 0.05)),2)
    print(f"Your incurred a cost of ${final} with extra charges of {round(extra_charges,2)} for {texts-50} extra minutes.\n Your sales tax was {sales_tax} and your 911 call charge was $0.44 ")
elif texts >50 and airtime >50:
    extra_charges = (0.15*(texts-50)) +(0.25*(airtime-50))
    total = (extra_charges + 0.44 + 15)
    sales_tax= round(total*0.05,2)
    final = round((total+ (total * 0.05)),2)
    print(f"Your incurred a cost of ${final} with extra charges of {round(extra_charges,2)} for {texts-50}.\n Your sales tax was {sales_tax} and your 911 call charge was $0.44 ")        