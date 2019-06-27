# 1. Uppercase a String
# Given a string, print the string uppercased.

string = input('Enter a word: ')
sstring = str(string).upper()
print(sstring)

# 2. Capitalize a String
# Given a string, print the string capitalized.

string2 = input('Enter a word: ')
sstring2 = str(string2).capitalize()
print(sstring2)

# 3. Reverse a String
# Given a string, print the string reversed.

oldlist = []
newlist = []

def reverse(attempt):
    for x in sword:
        oldlist.append(x)
    counter = 1
    for x in oldlist:
        newlist.append(oldlist[len(sword) - counter])
        counter += 1

word = input('Input a word: ')
sword = str(word)
reverse(sword)

for y in newlist:
    print(y),

# 4. Leetspeak
# Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need
# to replace make the following character replacements (treat all input characters as uppercase):
# 
# A => 4 E => 3 G => 6 I => 1 O => 0 S => 5 T => 7
# Example: Leet => l337

string3 = input('Which word do you want to translate? ')
sstring3 = str(string3)
firstlist = []
leetlist = []
for x in sstring3:
    firstlist.append(x)
for x in firstlist:
    if x == 'A':
        x = '4'
    elif x == 'E':
        x = '3'
    elif x == 'G':
        x = '6'
    elif x == 'I':
        x = '1'
    elif x == 'O':
        x = '0'
    elif x == 'S':
        x = '5'
    elif x == 'T':
        x = '7'
    leetlist.append(x)

for x in leetlist:
    print(x),

# 5. Long-long Vowels
# Given a word as a string, print the result of extending any long vowels to the length of 5. Examples:
# 
# Good => Goooood Cheese => Cheeeeese Man => Man Spoon => Spooooon

vowellist = []
newvowellist = []

string4 = input('Enter another word: ')
sstring4 = str(string4).lower()
for x in sstring4:
    vowellist.append(x)
find1 = 'ee'
find2 = 'oo'

sstring5 = str(string4)
for x in sstring5:
    newvowellist.append(x)

if sstring4.find(find1) != -1:
    newvowellist.insert(sstring4.find(find1), 'e')
    newvowellist.insert(sstring4.find(find1), 'e')
    newvowellist.insert(sstring4.find(find1), 'e')
elif sstring4.find(find2) != -1:
    newvowellist.insert(sstring4.find(find2), 'o')
    newvowellist.insert(sstring4.find(find2), 'o')
    newvowellist.insert(sstring4.find(find2), 'o')

for x in newvowellist:
    print(x),

# 6. Caesar Cipher
# Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar Cipher? 
# http://practicalcryptography.com/ciphers/caesar-cipher/
# 
# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s','t','u','v','w','x','y','z']
tring6 = input('Enter any string: ')
string6 = str(tring6)
shift = input('Enter your shift amount: ')
ishift = int(shift)

firstentry = []
deciphered = []

for x in string6:
    firstentry.append(x)
for x in firstentry:
    finder = alphabet.index(x)
    y = finder + ishift
    if y > 26:
        quicksave = y - 26
        y = quicksave
    z = alphabet[y]
    deciphered.append(z)
for x in deciphered:
    print(x),