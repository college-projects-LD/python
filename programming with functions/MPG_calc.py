def main():
    s_odometer = float(input('please enter the starting odometer reading here: '))
    e_odometer = float(input('please enter the ending odometer reading here:'))
    gal_used = float(input('How many US Gallons were used?: '))
    mpg = MPG_calculation(s_odometer, e_odometer, gal_used) 
    lp_100k = lp_100k_converter(mpg)

    print(f'this vehicle acheived a fuel economy of {mpg:.2f} MPG / {lp_100k:.2f} liters per 100k')
    pass

def MPG_calculation(s_odometer, e_odometer, gal_used):
    mpg = ((e_odometer - s_odometer) / gal_used)

    return mpg

def lp_100k_converter(mpg):
    lp_100k = (235.215 / mpg)
    return lp_100k

main()
