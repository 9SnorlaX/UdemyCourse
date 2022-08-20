#Sudoku

def any_duplicates(square):
    plain = [i for x in square for i in x]
    return sorted(plain) != [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(any_duplicates([[1, 3, 2], [9, 7, 8], [4, 5, 6]]))
print(any_duplicates([[1, 1, 3], [6, 5, 4], [8, 7, 9]]))