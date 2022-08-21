import math
#PAYE Tax Calculator!

income = float(input("Enter your income: "))

#income less than 25000
if income > 0 and income < 25000:
    paye =0

#income less than 250000 and greater than 350000
elif income > 250000 and income < 350000:
    paye =0.1*(income-250000)

#income less than 450000 and greater than 350000
elif income < 450000 and income > 350000:
    paye =10000 + (0.2*(income-350000))
#income if none of the above
else:
    paye =30000 + (0.3*(income-450000))
print("PAYE Tax = ",paye) 