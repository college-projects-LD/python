age = int(input( 'How old are you? '))
new_age = age + 1
egg_cartons = int(input('How many egg cartons do you have? '))
eggs = egg_cartons * 12
cookie_num = int(input('How many cookies are there? '))
people_num = int(input('How many people are present? '))
cookie_div = cookie_num / people_num
print (f'You will be {new_age} on your next birthday')
print (f'You have {eggs} eggs')
print (f'Each person can have {cookie_div} Cookies')