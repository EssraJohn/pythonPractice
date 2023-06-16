# break
# continue
# enumerate

l = [10, 20, 30, 40, 50, 99]
key = int(input("Enter the key: "))

for value in l:
    if value == key:
        print("element found")
        break
    else:
        continue
else:
    print("Element not found")

for index, value in enumerate(l):
    if value == key:
        print("element found at index ", index)
        break
    else:
        pass
else:
    print("Element not found at any index")

count = 1
sum = 0
while count <= 20:
    sum = sum + count
    count = count + 1
    print(sum)
