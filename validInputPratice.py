#  For valid integer
name: str = input("Enter your name:")
while True:
    try:
        age: int = int(input("Enter your age:"))
        break
    except ValueError:
        print("Please enter valid age")
print("Your name is:", name)
print("Your age is:", age)
# For valid float, just change int to float and float takes both int and float values as input
