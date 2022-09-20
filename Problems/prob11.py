# using nested for loop
# for creating patterns
rows = int(input("Enter number of rows you want:"))
for i in range(1, rows + 1):
    for j in range(rows + 1, i, -1):
        print(" ", end=' ')     # we can print whatever symbol than * space, try whitespace
    for k in range(1, i + 1):
        print(k, " ", end=' ')
    print("\n")
