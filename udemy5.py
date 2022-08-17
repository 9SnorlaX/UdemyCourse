# Cycle, division on 3 or 5

limit = int(input("Enter the number"))
total_sum = 0
for x in range(limit + 1):
    if x % 3 == 0 or x % 5 == 0:
        total_sum += x
    else:
        continue
print(f'Total sum = {total_sum}')

#list comprehension

limit = int(input("Enter the number"))
total_sum = sum([x for x in range(limit + 1) if x % 3 == 0 or x % 5 == 0])
print(f'Total sum = {total_sum}')
