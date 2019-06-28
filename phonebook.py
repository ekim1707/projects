phoneBook = {'bob': '1232340980', 'chris': '0942094832', 'ben': '2302034989', 'david': '0293842304', 'jack': '2039482340'}
def lookUp():
    nameEntry = input('Enter name: ')
    lnameEntry = nameEntry.lower()
    print('Name: ' + nameEntry)
    print('Number: ' + phoneBook.get(lnameEntry))
def setEntry():
    newEntry = input('Enter name: ').lower()
    cnewEntry = newEntry.capitalize()
    newNumber = str(input('Enter number (no spaces): '))
    phoneBook[newEntry] = newNumber
def delete():
    newDelete = input('Enter name: ').lower()
    del phoneBook[newDelete]
def listEntries():
    print(phoneBook)

x = 0
while x == 0:
    firstInput = int(input('Electronic Phone Book \n=====================\n1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries \n5. Quit\nWhat do you want to do (1-5)? '))
    if firstInput == 1:
        lookUp()
    elif firstInput == 2:
        setEntry()
    elif firstInput == 3:
        delete()
    elif firstInput == 4:
        listEntries()
    elif firstInput == 5:
        break
    else:
        print('Sorry. Invalid answer.')

print('Bye.')