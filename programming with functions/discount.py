
from datetime import datetime

newsubtotal = 0
price = 1
number = 0
subtotal = 0
while price != 0:
    price = float(input('\nWhat is the price of the item?: '))
    number = int(input('How many items are to be added?: '))

    subtotal = price * number
    newsubtotal = newsubtotal + subtotal
    print(f"\nYour current subtotal before tax and any applicable discount is: ${newsubtotal:.2f}")

date_time = datetime.now()
day_of_week = date_time.weekday()

if day_of_week == 1 or day_of_week == 2:
    if newsubtotal >= 50:
        newsubtotal = newsubtotal *.90
else: 
    print("\nSorry, but the discount is only available on Tuesday and Wednesday if the total is over $50!")

tax = newsubtotal * .06

print(f'\nYour subtotal is: ${newsubtotal:.2f}') 
print(f'\nTax: ${tax:.2f}')
print(f'\nYour total is: ${newsubtotal+tax:.2f}')