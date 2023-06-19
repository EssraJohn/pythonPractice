""""# 3d array using list
x = int(input())
y = int(input())
z = int(input())
n = int(input())
total = []
for x_i in range(x + 1):
    for y_i in range(y + 1):
        for z_i in range(z + 1):
            if (x_i + y_i + z_i) != n:
                total.append([x_i, y_i, z_i])
print(total)"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())

lista = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]

print(lista)