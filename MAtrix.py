matrix = [
    [1,2,3],
    [2,3,4],
]
print(matrix)
print(matrix[0][2])
print(matrix[1][2])
matrix[0][1]= 3 # adding value
print(matrix[0][1])

#using nested loop
for row in matrix :
    for col in row:
        print(col)


