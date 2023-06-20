# Number pattern
row = int(input("Enter no of rows:"))
for y in range(row, 0, -1):
    for x in range(row, y-1, -1):
        print(x, end=' ')
    print("\n")

row = int(input("Input:"))
for x in range(row, 0, -1):
    for y in range(x, row+1):
        print(y, end=' ')
    print("\n")
