#Cycle
number = int(input("Number"))
for x in range(number):
    print('*' * (x + 1))

# odd\even for a range
number2 = int(input("Number"))
y = 0
while y <= int(number2):
    if y %2 == 0:
        print(f'{y} this number is even')
    else:
        print(f'{y} this number is odd')
    y += 1
