from datetime import datetime

import math

date_time = datetime.now()

print(f"{date_time:%Y-%m-%d}")

Width = float(input(" What is the With of the tire in MM: "))
Aspect = float(input(" What is the Aspect Ration of the tire: "))
Diameter = float(input(" What is th diameter of the tire in Inches: "))

Volume = (math.pi * (Width* Width) * Aspect *((Width * Aspect) + (2540 * Diameter)))/10000000000


with open("Tire_info.txt", "at") as tire_file:

    print(f"{date_time:%Y-%m-%d}, {Width}, {Aspect}, {Diameter}, {Volume:.2f}", file=tire_file)

print (f'This  tire has an approx. Volume of {Volume:.2f} Liters of air')
