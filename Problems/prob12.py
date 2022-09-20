# using nested for loop
# for creating patterns, same as prob 11, but in reverse order
rows = int(input("Enter number of rows you want:"))
for i in range(rows, 0, -1):
    for j in range(i, rows + 1):
        print(" ", end=' ')     # we can print whatever symbol than * space, try whitespace
    for k in range(1, i + 1):
        print(k, " ", end=' ')
    print("\n")
