# for loop
# Number patter in reverse
row = int(input("Enter no of rows:"))
for y in range(row + 1, 1, -1):
    for x in range(1, y):
        print(x, end=' ')
    print("\n")

# number pattern
row = int(input("Enter no of rows:"))
for y in range(1, row + 1, +1):
    for x in range(1, y+1):
        print(x, end=' ')
    print("\n")