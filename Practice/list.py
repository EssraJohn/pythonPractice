# LIST in python
listElements = [1, 2, 3, 4]

for elements in listElements:
    print(elements)


print("Elements in the list are", listElements)

# appending or adding an element to the list
# we can append only single element at once
listElements.append(50)
print("Elements in the list are", listElements, "after appending")

# Reversing the elements in the list
listElements.reverse()
print("Elements in the list are", listElements, "after reversing")

# insert element at your desired position
listElements.insert(12, 98)
print("Elements in the list are", listElements, "after inserting at desired position")

# insert element at your desired position
listElements.insert(4, 77)
print("Elements in the list are", listElements, "after inserting at desired position")

# It will sort the elements in the list if they are of same datatype
listElements.sort()
print("Elements in the list are", listElements, "after sorting")

# pop
listElements.pop(5)
print("Elements in the list are", listElements, "after pooping")

# clear
listElements.clear()
print("Elements in the list are", listElements, "after clearing")

# type
print(type(listElements))

