hotel = {
    '1': {
        '101': ['George Jefferson', 'Wheezy Jefferson']
        },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
        },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
        }
    }
x = 0
while x == 0:
    firstOption = int(input('Welcome to the Hotel. Main menu (1)Check in or check out (2)List hotel occupancy (3)Quit: '))
    if firstOption == 1:
        check = input('Check in or check out ("I" or "O")? ')    
        lcheck = check.lower()
        if lcheck == 'i':
            secondOption = input('Enter a floor number: ')
            thirdOption = input('Enter a room number: ')
            if thirdOption in hotel[secondOption]:
                print('Sorry. Already occupied.')
            else:
                fourthOption = input('How many occupants? ')
                fifthOption = input('What are their names (no commas)? ')
                lfifthOption = fifthOption.split()
                hotel[secondOption][thirdOption] = lfifthOption
        elif lcheck == 'o':
            secondOption = input('Enter a floor number: ')
            thirdOption = input('Enter a room number: ')
            if thirdOption in hotel[secondOption]:
                del hotel[secondOption][thirdOption]
            else:
                print('Sorry. That room is not currently occupied.')
        else:
            print('Sorry invalid answer.')
    elif firstOption == 2:
        print(hotel)
    elif firstOption == 3:
        break