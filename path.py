name = input('type your name')
print('welcome', 'to the path' , name)

answer = input('There is a big mountain, which way you want to go, left or right ?').lower()

if answer == 'left':
    answer = input('You come to a river and you can walk around or swim')

    if answer == 'swim':
        print('you swim across and were eaten by an fish ;(')
        quit()
    elif answer == 'walk':
        print('you walk and ran ut of water and dead')
    else :
        print('not a valid option')

elif answer == 'right':
    answer = input('You saw a friend will you say hello?')

    if answer == 'yes':
        answer = input('he invited you to a party , will you go there?')
        if answer == 'sure':
                print('You just met your future wife there!')
        elif answer == 'nope':
                print('You finally came to your home and say hello to your boring life')
        else :
                print('not a valid option')

    elif answer == 'no':
        print('You finally came your home and say hello to your boring life')
    else :
        print('not a valid option')
    
else :
    print('not a valid option')