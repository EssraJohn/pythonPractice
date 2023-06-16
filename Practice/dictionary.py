# DICTIONARY
keyValue = {1: 'Essra', 2: 'Sem', 3: 'Interview', 4: 'LBIT Labs', 5: 100}
print(keyValue)

# type
print(type(keyValue))
# delete an item from dictionary
del keyValue[2]
print(keyValue)

# delete method 2
keyValue.__delitem__(5)
print(keyValue)


