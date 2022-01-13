import math


number_of_items = int(input("How many Items are present?: "))

number_of_boxed_items = int(input('How many items are you placing in a box?: '))

def box_divison_system(i,b):
    r = i/b
    remainder = math.ceil(r)
    return remainder

number_of_boxes = box_divison_system(number_of_items, number_of_boxed_items)

print()

print(f'For {number_of_items} items, and {number_of_boxed_items} to a box, please use {number_of_boxes} boxes. ')

