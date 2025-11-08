units = int(input("Enter the amount of units you have used: "))
if units<50:
    amount = units*6
    tax = 60
elif units<=200:
    amount = units*9
    tax = 100
else:
    amount = units*15
    tax = 200
grandtotal = amount+tax
print("Your grandtotal is",grandtotal)
