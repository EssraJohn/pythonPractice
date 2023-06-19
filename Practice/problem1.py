# to find the string present who's length is greater than 4

example = "Python is used to connect to the database"
ex = example.split(" ")
results = []
for var in ex:
    if len(var) > 4:
        results.append(var)
print(results)
