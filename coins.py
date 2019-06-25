coins = 0
while coins >= 0:
    print('You have ' + str(coins) + ' coins.')
    wantanother = input('Do you want another? ').lower()
    if wantanother == 'yes' or wantanother == 'y':
        coins += 1
    elif wantanother == 'no' or wantanother == 'n':
        print ('Bye.')
        break
    else:
        print('Invalid answer! Try again.')