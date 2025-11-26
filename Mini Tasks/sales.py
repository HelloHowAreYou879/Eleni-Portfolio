sales=float(input("monthly sale amount?"))
if sales<=1000:
    commission=0
elif sales<=3000:
    commission=2
elif sales<=5000:
    commission=5
elif sales<=10000:
    commission=7
else:
    commission=10
print("commission: ",commission,"%")
