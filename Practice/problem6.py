# The provided code stub reads and integer nfrom STDIN. For all non-negative integers ,i < n, print i**2

n = int(input("Enter the integer:"))
i = 0
if i < n:
    for i in range(0, n):
        num = i ** 2
        print(num)
