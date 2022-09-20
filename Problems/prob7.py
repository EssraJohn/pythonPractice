# Problem 5
# for loop
# Number pattern
row = int(input("Enter no of rows:"))
for y in range(row, 0, -1):
    for x in range(y, 0, -1):
        print(x, end=' ')
    print("\n")
