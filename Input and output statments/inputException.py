# For invalid input we ask user again to enter the correct value using Exception Handling

while 1:
    try:
        age: int = int(input("what is your age?: "))
        break
    except ValueError:
        print("Enter only digit.")
        continue

# noinspection PyUnboundLocalVariable
print("age:", age)


"""
# Basic syntax for input validation
while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer!")
"""

