first_choice = input('You wake up in the middle of the woods. What do you do? Check your bag, Or look around? (CHECK / LOOK)')
if first_choice.upper() == 'CHECK':
    second_choice = input('In your bag you see two items of use right now, a Match and a Flash Light. Which do you take out of the bag? (MATCH/FLASHLIGHT)')
    if second_choice.upper() == 'MATCH':
        third_choice = input ('You strike the Match, It flickers for a moment and then goes out. Do you STACK wood for a fire or do you strike another match? (STACK/MATCH)')
        if third_choice.upper() == 'STACK':
            print(f'You wait to start a fire until you prepare the Firewood. You strike the match to set the Firewood ablaze the fire wood starts up quickly and in its light you see a short ledge that you must have fallen off of and you see your truck. You decide to stay the night by the \n fire. You return home the next morning.')
        elif third_choice.upper() == 'MATCH':
            print(f'You continue to strike matches until to your surprise you find that you have used them all. You decide to lay down where you are to spend a long cold night under the stars. The next morning the sun rises and in its light you see a short ledge that you must have fallen off of and you see your truck. You drive home safely ')
        elif third_choice.upper () == 'FLASHLIGHT':
            print (f''' You being a clever sort remember after a time that there is still a flashlight in your bag. 
You turn it on and in its light you see a short ledge that you must have fallen off of and you see
your truck. You drive home safely''')
        else:
            print(f''' Fine Have It Your Way. Rocks fall and you die, GAME OVER Try Again.''')
    elif second_choice.upper() =='FLASHLIGHT':
        print(f''' You remember after a time that there is still a flashlight in your bag. 
You turn it on and in its light you see a short ledge that you must have fallen off of and you see
your truck. You drive home safely''')
    else:
            print(f''' Fine Have It Your Way. Rocks fall and you die, GAME OVER Try Again.''')
elif first_choice.upper() == 'LOOK': 
    print(f''' You Stumble around in the darkness, After a time you come face to face with a cold dark object.
    after being scared for a few moments you gather your courage to find your truck. You get in and drive home safely. ''')
else:
      print(f''' Fine Have It Your Way. Rocks fall and you die, GAME OVER Try Again.''')