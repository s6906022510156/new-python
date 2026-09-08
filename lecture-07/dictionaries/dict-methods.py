phonebook = {'anirach':'777-1111' , 'mickey':'777-2222',
              'donald':'777-3333', 'pluto':'777-4444'}

heroesdict = {}
heroesdict['hulk'] = '888-1111'
heroesdict['iron man'] = '888-2222'
print(heroesdict.get('halk', 'key not found'))
print(heroesdict.get('hulk', 'key not found'))


for key, value in phonebook.items():
    print(key,value)


print(phonebook.keys())
print(phonebook.values())


print(phonebook.pop('mick', 'element not found'))
print(phonebook.pop('mickey', 'element not found'))
print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print('after clear')
print(phonebook)