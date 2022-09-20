# electricity bill calculation
ele = int(input("Enter the number of units:"))
if ele <= 50:
    ele1 = 60
if 50 < ele < 100:
    un1 = ele - 50
    ele1 = (un1 * 5) + 60
if ele > 100:
    un1 = ele - 100
    ele1 = (un1 * 10) + 310
print("total bill is", ele1)
