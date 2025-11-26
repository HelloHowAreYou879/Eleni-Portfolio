amountSpent=float(input("how much did u spend"))
if amountSpent<50:
    discount=0
elif amountSpent<100:
    discount=0.05
elif amountSpent<200:
    discount=0.10
elif amountSpent<500:
    discount=0.15
else:
    discount=0.20
discountAmount=amountSpent*(1-discount)
print(discountAmount)   
