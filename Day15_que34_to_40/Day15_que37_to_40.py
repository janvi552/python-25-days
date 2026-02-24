#write a python program to add two matrices

def add_matrices(mat1,mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "matrices must have the same dimensions"
    
    result=[]
    for i in range(len(mat1)):
        row=[]
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)

    return result

matrix1=[
    [1,2,3],
    [4,5,6],
    [6,7,8]
]

matrix2=[
    [7,8,9],
    [4,5,6],
    [1,2,3]
]

final=add_matrices(matrix1,matrix2)

if isinstance(final,str):
    print(final)

else:
    print("sum of two matrixs :")
    for row in final:
        print(row)


#write a python program to multiply two matrices

def multiple_matrices(mat1,mat2):
    row1 = len(mat1)
    col1 = len(mat1[0])
    row2 = len(mat2)
    col2 = len(mat2[0])

    if col1 != row2 :
        return "matrices multiplication is not possible. number of coloum"

    result= [[0 for _ in range(col2)] for _ in range(row1)]

    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j] += mat1[i][k]* mat2[k][j]

    return result

matrix1= [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2=[
    [7,8,9],
    [4,5,6],
    [1,2,3]
]

final = multiple_matrices(matrix1,matrix2)

if isinstance(final,str):
    print(final)

else:
    print("multiplication of two matrices :")
    for row in final:
        print(row)


#print a python program to transpose a matrix

def transpose_matrix(matrix):
    rows,cols=len(matrix),len(matrix[0])

    result=[[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result

mat=[
    [7,8,6],
    [2,4,1]
]

result_matrix=transpose_matrix(mat)

for row in result_matrix:
    print(row)


#write a python program to sort words in alphabetic order

string=input("enter a string :")

words=[word.capitalize() for word in string.split()]

words.sort()

print("the sorted words are :")
for word in words:
    print(word)









    