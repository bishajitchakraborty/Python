#user input row and column
row=int(input("Enter Your Row:"))
col=int(input("Enter Your Colomn:"))
#input matrix
matrix=[]
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input()))
    matrix.append(a)


#print matrix
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()