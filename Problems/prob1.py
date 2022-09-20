# Problem-1`
# double the apples given to each member
app1 = int(input("Enter the apple given to PP:"))
mul1 = 2 * app1     # double the apples given to pp
app2 = int(input("Enter the apple given to MK:"))
mul2 = 2 * (mul1 + app2)  # double the number of apples added with the number of apples from pp to mk
app3 = int(input("Enter the apple given to SV:"))
mul3 = 2 * (mul2 + app3)    # double the number of apples added with the number of apples from mk to sv
# Total number of apples
print("Total number of apples given to sir: {}".format(mul3))


""" a = 2
a = (a * 2)
b = 1
b = (a + b) * 2
c = 3
c = (b + c) * 2
print("Total number of apples given to sir: {}".format(c))
"""
