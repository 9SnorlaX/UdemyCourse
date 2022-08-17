#Joined 2 lists

first_list = [1, 3, 4, 6, 8, 5, 9, 11]
second_list = [2, 4, 6, 1, 7, 9, 10, 12]
joined_list = []

for x in first_list:
    if x % 2 != 0:
        joined_list.append(x)
for x in second_list:
    if x % 2 == 0:
        joined_list.append(x)
print(joined_list)

#list comprehension

first_list = [1, 3, 4, 6, 8, 5, 9, 11]
second_list = [2, 4, 6, 1, 7, 9, 10, 12]

odds = [x for x in first_list if x % 2 != 0]
evens = [x for x in second_list if x % 2 == 0]

joined_list = odds + evens
print(joined_list)
