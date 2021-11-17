# Instructions
# Hint: Look at the remote learning “Matrix” videos

# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, select only the alpha characters and connect them, then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix:

# 7i3
#     Tsi
#     h%x
#     i #
#     sM
#     $a
#     #t%
#     ^r!

matrix = [
    ["7", "i", "3"],
    ["T", "s", "i"],
    ["h", "%", "x"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"]
]

string = ''
columns = len(matrix[0])
rows = len(matrix)
for a in range(columns):
    for b in range(rows):
        if matrix[b][a].isalpha():
            string += matrix[b][a]
        elif string and string[-1] != ' ':
            string += ' '

print(string)
