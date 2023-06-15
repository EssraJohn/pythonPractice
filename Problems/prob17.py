# to find element in a list with user input
a = []
n = int(input("Enter the size of list:"))
print("Enter values:")
for i in range(0, n):
    x = int(input(""))
    a.append(x)
b = int(input("Enter integer to be found:"))
if b in a:
    print("element found")
else:
    print("element not found")
