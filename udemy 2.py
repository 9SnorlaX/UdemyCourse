x = input("first point")
y = input("Second point")

if int(x) >= int(y):
    raznica = int(x) - int(y)
if int(y) >= int(x):
    raznica = int(y) - int(x)

print(raznica)

x1 = int(input("enter x1"))
y1 = int(input("enter y1"))
x2 = int(input("enter x2"))
y2 = int(input("enter y2"))

distance = round(((x1-x2)**2 + (y1 - y2)**2) ** 0.5, 3)
print(distance)

import math
x1 = int(input("enter x1"))
y1 = int(input("enter y1"))
x2 = int(input("enter x2"))
y2 = int(input("enter y2"))

distance = round(math.sqrt((x1-x2)**2 + (y1 - y2)**2) ** 0.5, 3)
print(distance)

