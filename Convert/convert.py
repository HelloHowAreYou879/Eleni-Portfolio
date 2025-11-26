#initialises constants
POUNDS_TO_USD=1.4
POUNDS_TO_EUR=1.14
POUNDS_TO_BRL=4.77
POUNDS_TO_JYP=151.05
POUNDS_TO_TRY=5.68

UNDER300=0.035
OVER300=0.03
OVER750=0.025
OVER1000=0.02
OVER2000=0.015

DISCOUNT=0.05

#gets a valid amount of pounds to convert
def validate_pounds():
    while True:
        pounds=float(input("How many pounds do you want to convert? (1-2500)"))
        if 1<=pounds<=2500:
            return pounds
        else:
            print("Maximum of 2500 GDP can be converted in one transaction.")

#gets a valid currency to convert into
def validate_currency():
    while True:
        currency=input("What currency would you like to convert to? (usd/eur/brl/jpy/try) ")
        currency=currency.lower()
        if currency=="usd":
            return "usd"
        elif currency=="eur":
            return "eur"
        elif currency=="brl":
            return "brl"
        elif currency=="jpy":
            return "jpy"
        elif currency=="try":
            return "try"
        else:
            print("Invalid currency. Please enter either usd,eur,brl,jpy,try.")

#gets customer details        
name=input("Whats your name? ")
address=input("Whats your address? ")
phoneNumber=int(input("Whats your phone number? "))

pounds=validate_pounds()
currency=validate_currency()

#calculates amount of money after conversion
if currency=="usd":
    newAmount=pounds*POUNDS_TO_USD
elif currency=="eur":
    newAmount=pounds*POUNDS_TO_EUR
elif currency=="brl":
    newAmount=pounds*POUNDS_TO_BRL
elif currency=="jyp":
    newAmount=pounds*POUNDS_TO_JYP
else:
    newAmount=pounds*POUNDS_TO_TRY


#transaction fee
if pounds<300:
    transactionFee=UNDER300*pounds #0-300
elif pounds<750:
    transactionFee=OVER300*pounds #300-750
elif pounds<1000:
    transactionFee=OVER750*pounds #750-1000
elif pounds<2000:
    transactionFee=OVER1000*pounds #1000-2000
else:
    transactionFee=OVER2000*pounds #2000+

totalCost=transactionFee+newAmount

staff=input("Are you a memeber of staff? ")
if staff.lower()=="yes":
    discountedAmount=round(totalCost*(1-DISCOUNT),2)
    print("You get a 5% discount! ")
else:
    discountedAmount=round(totalCost,2)

#print receipt
print("\n--- Order Summary ---")
print(f"Customer Name: {name}")
print(f"Address: {address}")
print(f"Phone Number: {phoneNumber}")
print("Converted amount: " , newAmount)
print("Transaction Fee: ",transactionFee)
print("Total Cost: ",totalCost)
print("Discounted amount: ",discountedAmount)
print("----------------------")




    

