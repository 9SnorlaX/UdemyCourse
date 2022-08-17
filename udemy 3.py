#Count legs
chiken_legs = 2
goat_legs = 4
cow_legs = 4

chiken = input("How many?")
goat = input("How many")
cow = input("How many")
count_of_legs = (chiken_legs * int(chiken)) + (goat_legs * int(goat)) + (cow_legs * int(cow))
print("In farm", count_of_legs, "animal legs")
