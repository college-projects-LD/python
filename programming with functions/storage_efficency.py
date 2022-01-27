
import math

def main():
    numberOfCans=int(input('How many sizes do you need: '))
    list = []
   
    for i in range(numberOfCans):
        
        radius = float(input('Please enter the radius of the can in Centimeters: '))
        height = float(input('Please enter the height of the can in Centimeters: '))
        volume = compute_volume(radius, height)
        surface = compute_surface_area(radius,height)
        storage = compute_storage_efficiency(volume,surface)
        list.append(storage)
            
            
        #for i in range(numberOfCans):
        print(f' Storage Efficiency: {storage:.1f} ')


def compute_volume(radius, height):
    volume = math.pi * (radius**2) * height
    return volume


def compute_storage_efficiency(v,sA):
    storage = v / sA
    return storage


def compute_surface_area(radius, height):
    surface_area = (2*math.pi*radius)*(radius+height)
    return surface_area

main()

#week_ten_list = []

#cart = None

#print('\nPlease enter the items of the shopping list (type: quit to finish): ')

#while cart != 'quit':
    #cart = input('Item: ')
   # if cart == 'quit':
      #  continue 
    #else:
       # week_ten_list.append(cart)

#----
#print('\nThe shopping list is:')

#for output in week_ten_list:
    #print(output)

