# Ordering till the error

shouldnot="pumpkin spice latte"

val=True
order_count=0
while val:
    order=input("Enter your order :- ")
    if order.lower()==shouldnot:
        print("Total order :- ",order_count)
        break
    else:
        print("Your order :- ",order)
        order_count+=1