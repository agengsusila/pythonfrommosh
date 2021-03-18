matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[1][2] = 40 #To modify a value of list, the 1st squarebrackets is for list, and the 2nd is the item.
for row in matrix:
    for item in row:
        print(item)
