# Exercise 1

phonebook_dict = { 
  'Alice': '703-493-1834', 
  'Bob': '857-384-1234', 
  'Elizabeth': '484-584-2923'
}
print(phonebook_dict['Elizabeth'])
phonebook_dict['Kareem'] = '938-489-1234'
del phonebook_dict['Alice']
phonebook_dict.update({'Bob':'968-345-2345'})
print(phonebook_dict)

# Exercise 2: Nested Dictionaries

ramit = { 
  'name': 'Ramit', 
  'email': 'ramit@gmail.com', 
  'interests': ['movies', 'tennis'], 
  'friends': [ 
     { 
       'name': 'Jasmine', 
       'email': 'jasmine@yahoo.com', 
       'interests': ['photography', 'tennis']
     }, 
     { 
        'name': 'Jan', 
        'email': 'jan@hotmail.com', 
        'interests': ['movies', 'tv'] 
     } 
    ] 
}
print(ramit.get('email'))
print(ramit['interests'][0])
print(ramit['friends'][0]['email'])
print(ramit['friends'][1]['interests'][1])

# Letter Summary

word = input('Enter a word: ')
wordList = []
alphabetDict = {'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0, 'g': 0, 'f': 0, 'i': 0, 'h': 0, 'k': 0, 'j': 0, 'm': 0, 'l': 0, 'o': 0, 'n': 0, 'q': 0, 'p': 0, 's': 0, 'r': 0, 'u': 0, 't': 0, 'w': 0, 'v': 0, 'y': 0, 'x': 0, 'z': 0}
alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for y in word:
    wordList.append(y)
listcounter = 1
wordcounter = 0
while wordcounter < len(word):
    for x in alphabetList:
        if x == wordList[wordcounter]:
            alphabetDict[x] += 1
    wordcounter += 1
print(alphabetDict)

# Word Summary

paragraph = input('Enter your paragraph: ')
histolist = paragraph.split()
dictlist = {}
for x in histolist:
    dictlist[x] = 0
wordcounter = 0
for x in histolist:
    if x == histolist[wordcounter]:
        dictlist[histolist[wordcounter]] += 1
    wordcounter += 1
print(dictlist)

# Bonus Challenge
# Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters.