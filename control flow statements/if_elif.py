# if-elif statements
a: int = int(input("Enter any number:"))
if a <= 100:
    print("A lies below 100")
elif 100 <= a <= 1000:    # a >= 100 and a < 1000
    print("A is greater than 100 and less than 1000")
elif 1000 <= a <= 10000:
    print(" A is greater than 1000")
else:
    print("A is not present")
