# if else in list comprehension
i: int = int(input("Enter a digit:"))
if 10 != i:
    print("{} is not equal to key".format(i))
else:
    # first if statement
    if i < 15:
        print("%d is smaller than 15" % i)
        # Nested - if statement
        # Will only be executed if statement above
        # it is true
    if i < 12:
        print("%d is smaller than 12 too" % i)
