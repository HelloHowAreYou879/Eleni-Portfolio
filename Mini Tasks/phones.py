price=float(input("phone price? "))
cond=input("is it excellent,good,ok,poor ")
if cond=="excellent":
    resale=0.7
elif cond=="good":
    resale=0.55
elif cond=="ok":
    resale=0.4
else:
    resale=0.2
print(round( price*(1-resale),2 ) )
