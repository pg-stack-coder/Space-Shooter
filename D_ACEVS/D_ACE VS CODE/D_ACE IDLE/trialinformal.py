
######MATRIX ADDITION
'''l=[[j for j in range(1,5)]for i in range(1,4)]'''
'''for i in range (2):
    for j in range(5):
        l[i][j]=int(input('enter number:'))'''
'''b=[[j for j in range(1,5)]for i in range(1,4)]'''
'''for i in range (2):
    for j in range(5):
        b[i][j]=int(input('enter number:'))'''
'''c=[[' ' for j in range(1,5)]for i in range(1,4)]
for i in range (3):
    for j in range(4):
        c[i][j]=l[i][j]+b[i][j]
print(c)'''

###MATRIX MULTIPLICATION
'''n=int(input('enter the number of columns of A:'))
p=int(input('enter the number of colums of B:'))
m=int(input('enter the number of rows of A:'))
l=[[j for j in range(n)]for i in range(m)]
b=[[j for j in range(p)]for i in range(n)]
c=[[' ' for j in range(p)]for i in range(m)]
print(l)
print(b,'b')
for i in range(m):
    for j in range(p):
        c[i][j]=0
        for k in range(n):
            c[i][j]+=l[i][k]*b[k][j]
print(c)'''

###QUESTIONS ON CONCEPPT OOFFFFFk 2 DACE LIST
'''a=[ i for i in range(1,17)]
b=[[' ' for j in range(4)]for i in range(4)]
n=0
for i in range (4):
    for j in range(4):
        b[i][j]=a[n]
        n+=1
for i in b:
    print(i)'''

####QUESTION 2
'''a=[ i for i in range(1,17)]
b=[[' ' for j in range(4)]for i in range(4)] 
n=0
for i in range (4):
    for j in range(4):
        b[j][i]=a[n]
        n+=1
print(b)'''

####QUESTION 3 PART !
'''a=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
l=[]
for i in range (4):
    for j in range(4):
        m=a[i][j]
        l.append(m)
print(l)'''

####QUESTION 3 PART 2
'''a=[[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
l=[]
for i in range (4):
    for j in range(4):
        m=a[j][i]
        l.append(m)
print(l)'''

####QUESTION 4
'''f=1;s=c=n=0
l=[]
l.append(s)
while c!=15:
    t=f+s
    l.append(t)
    f,s=s,t
    c+=1
b=[[' ' for j in range(4)]for i in range(4)]
for i in range (4):
     for j in range(4):
        b[i][j]=l[n]
        n+=1
print(b)'''
    
###QUESTION 5 REMOVE DUPLICATE
'''a=[[1,2,3,4],[2,3,4,5],[1,5,7,9]]
for i in a:
    for j in i:'''
                
       
        


















        
        
        
















    
