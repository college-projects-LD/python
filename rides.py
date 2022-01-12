two_riders = input('Are there Two Riders? (Y/N): ')
first_age = int (input('What is the First riders Age In Years? '))
first_hight = int(input('What is the First Riders Hight in Inches? '))
if first_hight < 36:
   hight = False
else:
    hight = True


if two_riders.upper() == 'Y':
    second_age = int (input('What is the Second riders Age In Years? '))
    second_hight = int(input('What is the Second Riders Hight in Inches? '))
    if second_hight < 36:
          hight = False
    else: 
        hight = True
   
if first_age >= 18:
    age = True
else:
    age = False


if hight and age:
    print(f'Have fun And Remember To Keep Your Arms and Legs Inside The Vehicle At All Times')
else:
     print (f'I\'m sorry but you may not ride')
