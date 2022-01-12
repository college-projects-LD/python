from datetime import datetime

current_date =datetime.now()
week_day = current_date.weekday()

subtotal=float(input('What is the Subtotal?: '))
grand_total = float(0)
if subtotal >= 50:
    if week_day == 1 or week_day ==2 :
        subtotal = subtotal *0.90
    else:
        print("i'm sorry but the discount is only offered on Tuesday and Wednesday")


else :
    print(f"i'm sorry but you need to purchase ${50-subtotal} more to qualify for the 10% discount")
tax = round (subtotal *.06, 2)
grand_total = subtotal + tax

grand_total =round(grand_total,2)

print(f'Sales tax: ${tax}')
print(f'Your total is ${grand_total} thank you for shopping with us today,Please come again!')
