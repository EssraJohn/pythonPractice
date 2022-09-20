# to calculate the bill
a = int(input("Enter the amount of onions you need:"))
if a <= 5:
    tot = a * 10
    print(f"Bill amount is {tot}")
else:
    pass
if 5 < a <= 10:
    tot = a * 8
    print(f"Bill amount is {tot}")
else:
    pass
if a > 10:
    tot = a * 6
    print(f"Bill amount is {tot}")
else:
    pass
print("Thank you,Visit again")
