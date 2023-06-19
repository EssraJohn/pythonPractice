# DICTIONARY
keyValue = {8: 'Essra', 2: 'Sem', 31: 'Interview', 4: 'LBIT Labs', 5: 100}
print(keyValue)

# type
print(type(keyValue))
# delete an item from dictionary
del keyValue[2]
print(keyValue)

# delete method 2
keyValue.__delitem__(5)
print(keyValue)
# sorted function
print((sorted(keyValue.items())))
