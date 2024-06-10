'''b=a
#Binary to decimal
if x=='b' and y=='d':
    a.reverse()
    v=0
    sum=0
    for i in a:
        s=int(i)*(2**v)
        sum+=s
        v+=1
    print(sum,'is the decimal number')
#o to d
elif x=='o' and y=='d':    
    a=b
    a.reverse()
    v=0
    sum=0
    for j in a:
        s=int(j)*(8**v)
        sum+=s
        v+=1
    print(sum,'is the decimal number')
#h to d
elif x=='h' and y=='d':
    a=b
    v=0
    sum=0
    for j in a:
        if j=='A':
            j=10
        elif j=='B':
            j=11
        elif j=='C':
            j=12
        elif j=='D':
            j=13
        elif j=='E':
            j=14
        elif j=='F':
            j=15
        s=int(j)*(16**v)
        sum+=s
        v+=1
    print(sum,'is the decimal number')

k=n
l=n  
if x=='d' and y=='b':
    m=[]
    while n!=0:
        a=n%2
        m.append(a)
        n//=2
    m.reverse()
    for i in m:
        print(i,end='')
    print(' is the binary number')
elif x=='d' and y=='o':
    m=[]
    while k!=0:
        a=k%8
        m.append(a)
        k//=8
    m.reverse()
    for i in m:
        print(i,end='')
    print(' is the octal number')
elif x=='d' and y=='h':
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
    print(' is the hexadecimal number')
elif x=='b' and y=='o':
    a.reverse()
    v=0
    sum=0
    for i in a:
        s=int(i)*(2**v)
        sum+=s
        v+=1
    m=[]
    while k!=0:
        a=k%8
        m.append(a)
        k//=8
    m.reverse()
    for i in m:
        print(i,end='')'''

a=input('enter the number:')
z=list(a)
x=int(input('enter from which base:'))
y=int(input('enter to which base:'))
z.reverse()
o=['A','B','C','D','E','F']
m=[]
k=0;l=0
for i in z:
    if i in o:
        k+=(10+o.index(i))*x**l
    else:
        k+=int(i)*x**l
    l+=1
while k!=0:
    j=k%y
    k//=y
    m.append(j)
m.reverse()
for j in m:
    if j>=10:
        print(o[j-10],end='')
    else:
        print(j,end='')











