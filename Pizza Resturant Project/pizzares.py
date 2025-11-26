#Defining constants
SMALL_PIZZA_PRICE = 3.25
MEDIUM_PIZZA_PRICE = 5.50
LARGE_PIZZA_PRICE = 7.15
DELIVERY_CHARGE = 2.50
EXTRA_TOPPINGS_PRICE1 = 0.75
EXTRA_TOPPINGS_PRICE2 = 1.35
EXTRA_TOPPINGS_PRICE3 = 2 
EXTRA_TOPPINGS_PRICE4 = 2.5
DISCOUNT = 0.1

#calculating price of each individual pizza
def get_pizza_cost(size,extraToppings):
    price=0
    if size=="small":
        price=price+SMALL_PIZZA_PRICE
    elif size=="medium":
        price=price+MEDIUM_PIZZA_PRICE
    else:
        price=price+LARGE_PIZZA_PRICE
    if extraToppings==0:
        pass
    elif extraToppings==1:
        price=price+EXTRA_TOPPINGS_PRICE1
    elif extraToppings==2:
        price=price+EXTRA_TOPPINGS_PRICE2
    elif extraToppings==3:
        price=price+EXTRA_TOPPINGS_PRICE3
    else:
        price=price+EXTRA_TOPPINGS_PRICE4
    return price
    
def validate_quantity():
    while True:
        quantity=int(input("How many pizzas would you like to order? (1-6) "))
        if 1<=quantity and quantity<=6:
            return quantity
        print("You can only order 1-6 pizzas.")

#getting customer details
def get_details():
    name=input("customer name: ")
    address=input("address: ")
    phone=input("phone number: ")
    return name,address,phone

def main():
    total=0
    name,address,phone=get_details()
     
    #getting pizza information and calcualting price
    quantity=validate_quantity()
    for i in range (1,quantity+1):
        print("Pizza ",i)
        size=input("Large,medium or small: ")
        toppings=input("Would you like extra toppings? ")
        if toppings.lower()=="yes":
            extraToppings=int(input("How many extra toppings? "))
        else:
            extraToppings=0
        pizzaPrice=get_pizza_cost(size,extraToppings)
        print("Pizza price: " , pizzaPrice)
        total=total+pizzaPrice
        
    #discount applied
    if total>=20:
        total=total*(1-DISCOUNT)
        print("You got a discount of" ,DISCOUNT*100 , "% off!")
        
    #handling delivery charge
    delivery=input("do you want delivery? ")
    if delivery=="yes":
        print("Delivery charge: ",DELIVERY_CHARGE)
        total=total+DELIVERY_CHARGE

    #outputting final bill    
    print("\nName: " , name , "\nAddress: ", address , "\nPhone: " , phone )
    print("total: ",total)

main()

