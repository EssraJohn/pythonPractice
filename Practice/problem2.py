# To find the prime numbers
import math
a: int = int(input("Enter number :"))
if a > 1:
    for num in range(2, int(math.sqrt(a)) + 1):
        if (num % 2) == 0:
            print(num, "  times", a//num, "a  number", a)
            break
        else:
            print(" not a Prime number")
print(" {} is the number". format(a))



