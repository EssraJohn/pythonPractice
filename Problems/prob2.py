# using if condition
# if cond should satisfy , the minus the 5
app1 = int(input("Enter the apple given to PP:"))
if app1 > 5:
    app1 = app1 - 5
print("no of apples left is ", app1)

app2 = int(input("Enter the apple given to MK:"))
app2 = (app1 + app2)
if app2 > 10:
    app2 = app2 - 10
print("no of apples left is ", app2)

app3 = int(input("Enter the apple given to GVM:"))
app3 = (app2 + app3)
if app3 > 20:
    app3 = app3 - 20
    print("Total number of apples given to sir: {}".format(app3))
print("No apples are left is", app3)
