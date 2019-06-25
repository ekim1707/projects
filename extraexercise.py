name = input('Enter your name: ')
strname = str(name)
if len(name) > 10:
    print('Wow, that\'s a long name')
else:
    print('Hello ' + strname + "!")

name1 = input('Enter three names of different length. \n1: ')
sname1 = str(name1)
lname1 = len(name1)
name2 = input('2: ')
sname2 = str(name2)
lname2 = len(name2)
name3 = input('3: ')
sname3 = str(name3)
lname3 = len(name3)

nameList = [lname1, lname2, lname3]
nameList.sort()
if nameList[0] == lname1:
    print('Hello ' + sname1 + '!')
elif nameList[0] == lname2:
    print('Hello ' + sname2 + '!')
elif nameList[0] == lname3:
    print('Hello ' + sname3 + '!')

print('1. Apples \n2. Oranges \n3. Androids')
number = input('Enter 1, 2, or 3: ')
intnum = int(number)

if intnum == 1:
    print('Apples are delicious!')
elif intnum == 2:
    print('Oranges are very good for you!')
elif intnum == 3:
    print('Androids are better than iPhones.')
else:
    print('Sorry...')

