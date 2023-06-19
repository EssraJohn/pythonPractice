# importing random
from random import *

# taking input from user
user_pass = int(input("Enter the Length of OTP "))

# storing alphabet letter to use thm to crack password
password = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]

# initializing an empty string
otp = ""

for letter in range(user_pass):
    guess_letter = password[randint(0, 9)]
    otp = str(guess_letter) + str(otp)

print(otp)

# printing the matched password
print("OTP is", otp)
