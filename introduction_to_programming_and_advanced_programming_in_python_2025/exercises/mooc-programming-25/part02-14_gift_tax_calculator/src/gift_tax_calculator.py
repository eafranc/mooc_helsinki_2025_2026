# Write your solution here
gift = float(input("Value of gift:"))

if(gift<5000):
    tax = 0
elif(5000<=gift<25000):
    low          = 5000
    tax_lower    = 100
    tax_exceding = 0.08

elif(25000<=gift<55000):
    low          = 25000
    tax_lower    = 1700
    tax_exceding = 0.10

elif(55000<=gift<200000):
    low          = 55000
    tax_lower    = 4700
    tax_exceding = 0.12

elif(200000<=gift<1000000):
    low          = 200000
    tax_lower    = 22100
    tax_exceding = 0.15

else:
    low          = 1000000
    tax_lower    = 142100
    tax_exceding = 0.17


if (gift<5000):
    print("No tax!")
else:
    # Tax Calculation for all ranges in the Tax Table
    tax = (tax_lower+(gift-low)*tax_exceding)    
    print(f"Amount of tax: {tax} euros")