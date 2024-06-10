l2=[[j for j in range(1,5)]for i in range(1,4)]  #3 row , 4 columns
print(l2)
l=[[j for j in range(1,4)]for i in range(1,3)] #2 rows, 3 columns
print(l)
mat=[[' ' for j in range(1,4)]for i in range(1,4)] #3 row , 3 columns
print(mat)
mul=1;sum=0
for i in range(3):
    for j in range(3):
        mul=l[i][j]*l2[j][i]
        sum+=mul
    mat[i][j]=sum
print(mat)