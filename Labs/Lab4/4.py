list = [ 4.95, 9.95, 14.95,19.95,24.95]
for x in list:
    discount = round((0.6 * x),2)
    new_price = round((0.4 * x),2)
    print(f"Original price : {x} , Discount Amount : {discount}, New Price : {new_price}")


