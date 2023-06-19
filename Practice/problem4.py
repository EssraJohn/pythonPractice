# Leap year
"""The year can be evenly divided by 4, is a leap year, unless:
1.The year can be evenly divided by 100, it is NOT a leap year, unless:
2.The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
 while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years"""
year = int(input("Enter the year: "))

# check if it is a century 100

if (year % 100 == 0) and (year % 4 == 0) and (year % 400 == 0):
    print(f"{year} is a leap year")
elif (year % 100 != 0) and (year % 4 == 0):
    print(f" {year} is a leap year")
else:
    print(f"{year} is a not a leap year")
