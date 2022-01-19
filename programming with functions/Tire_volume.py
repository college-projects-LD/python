from datetime import datetime

import math

date_time = datetime.now()

print(f"{date_time:%Y-%m-%d}")
phone_number = 0
Width = float(input(" What is the With of the tire in MM: "))
Aspect = float(input(" What is the Aspect Ratio of the tire: "))
Diameter = float(input(" What is the Diameter of the tire in Inches: "))

Volume = (math.pi * (Width* Width) * Aspect *((Width * Aspect) + (2540 * Diameter)))/10000000000

print (f'This  tire has an approx. Volume of {Volume:.2f} Liters of air')

ask_for_purchase = input('Would you like to purchase these tires? (yes/no) :')

if ask_for_purchase.lower() == 'yes':
    
    phone_number = int(input('Please enter your phone number without spaces (ex. 2086813692) so a member of our sales team can contact you to go over the details: '))
    with open("volumes.txt", "at") as volume_file:
        print(f"{date_time:%Y-%m-%d}, {Width}, {Aspect}, {Diameter}, {Volume:.2f}, phone number #{phone_number}", file=volume_file)

with open("volumes.txt", "at") as volume_file:

    print(f"{date_time:%Y-%m-%d}, {Width}, {Aspect}, {Diameter}, {Volume:.2f}", file=volume_file)