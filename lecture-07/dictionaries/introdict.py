phonebook = {'anirach': '777-1111', 'mickey': '777-2222','donald':'777-3333'}

print(phonebook)

print(phonebook['mickey'])
print(phonebook.get('donald'))

key = 'pluto'
if key in phonebook:
    print(phonebook['pluto'])
else:
    print(key + 'not in phonebook')


phonebook['simpson'] = '777-4567'
phonebook['pluto'] = '777-4444'
phonebook['mickey'] = '777-2122'
print(phonebook)

del phonebook['simpson']
print(phonebook)