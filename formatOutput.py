# Formatting String literal
# F-strings or Literal String Interpolation
name = input("My name is :")
print(f"Hi {name}! It's a pleasure to see you again {name}")

# Format as a Function
a = 5
b = 23
sum = a + b
print("The value of a is {} and b is {}".format(a, b))
print("Sum {2},is the addition of {0} and {1}".format(a, b, sum))
