'''x=[1,2,3,67,8.9,[[1],8,9]]
x[0]='dace'
print(x[-1:-5])
print(x[5][0][0])
x.append('dace')
print(x)
x=[]
for i in range(2,101,2):
    x.append(i)
print(x)
x=[1,2,3,4]
s=[2,100000,3555666]
print(x+s)
print(x*20)
y=[]
for i in range(0,4):
    y.append(x[i])
    y.append(x[i])
print(y)'''

'''n=int(input('enter a number in decimal:'))
k=n
l=n
m=[]
while n!=0:
    a=n%2
    m.append(a)
    n//=2
m.reverse()
for i in m:
    print(i,end='')
print(' is the binary number')

m=[]
while k!=0:
    a=k%8
    m.append(a)
    k//=8
m.reverse()
for i in m:
    print(i,end='')
print(' is the octal number')

m=[]
while l!=0:
    a=l%16
    if a==10:
        a='A'
    elif a==11:
        a='B'
    elif a==12:
        a='C'
    elif a==13:
        a='D'
    elif a==14:
        a='E'
    elif a==15:
        a='F'
    m.append(a)
    l//=16
m.reverse()
for i in m:
    print(i,end='')
print(' is the hexadecimal number')'''
#MATRICES
'''p=[]
l=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(l)):
    s=0
    for j in range(len(l)):
        s+=l[i][j]
    l[i].append(s)
for i in range(len(l)):
    s=0
    for j in range(len(l)):
        s+=l[j][i]
    p.append(s)
l.append(p)
s=0
for i in range(len(l)-1):
    s=s+l[i][i]
l[i+1].append(s)
for i in l:
    print(i,end='\n')'''

'''for i in range(len(l)):
    s+=l[i][len(l)-i-1]
l.append(s)
print(l)'''
#lower and upper triangular
'''s=v=0
for i in range(len(l)):
    for j in range(i):
        s+=l[i][j]
        v+=l[j][i]
        print(v,'rtm',end=',')
        print(s,'ltm')
print(s,'Left triangular matrix')
print(v,'right triangular matrix')'''
d=0
p=[]
l=[[1,2,3],[4,5,6]]
for i in range(len(l)):
    for j in range(len(l)):
        d=l[j][i]-d
    p.append(d)
l.append(p)
print(l)
















