'''x=list(input('enter:'))
l=[]
for i in x:
    if i in l:
        continue
    else:
        l.append(i)
for j in l:
    print(j,end=',')'''

'''x=list(input('enter:'))
for i in x:
    if int(i)==0:
        x.pop(x.index(i))
        x.append(i)
print(x)'''

'''x=input('enter the number:')
l=[]
c=[]
for i in x:
    y=x.count(i)
    if i in l:
        continue
    else:
        l.append(i)
        c.append(y)
print(l)
print(c)'''


'''x=list(input('enter the number:'))
mx=max(x)
f=0
for i in x:
    if int(i)>int(f) and i<mx:
        f=i
print(f)'''


'''x=list(input('enter a number:'))
min=10
for i in x:
    if int(i)<min:
        min=int(i)
print(min)'''

'''x=list(input('enter a number:'))
y=min(x)
f=10
for i in x:
    if int(i)>int(y) and int(i)<int(f):
        f=i
print(f,'is the second least number')'''
'''l=[]
for i in range(1,27):
    l.append(chr(96+i)*i)
print(l)'''

'''x=list(input('enter a number:'))
for i in range(0,len(x)//2+1):
    x[i],x[len(x)-1-i]=x[len(x)-1-i],x[i]
print(x)'''

'''x=list(input('enter a number:'))
for i in range(len(x)):
    f=min(x[i:])
    x.remove(f)
    x.insert(i,f)
    print(x)'''

#selection sort
l=list(input('enter a number:'))
for i in range (len(l)):
    small=l[i];pos=i
    for j in range(i,len(l)):
        if l[j]<small:
            small=l[j]
            pos=j
    l.pop(pos)
    l.insert(i,small)
    print(l)

#exchange selection sort
l=list(input('enter a number:'))
for i in range (len(l)):
    small=l[i];pos=i
    for j in range(i,len(l)):
        if l[j]<small:
            small=l[j]
            pos=j
    l[i],l[pos]=l[pos],l[i]
    print(l)



'''l=eval(input('enter a number:'))
x=list(l)
for i in l:
    if str(i)==str(i[::-1]):
        print(x)'''
'''l=[]

for i in range(3,100,2):
    l.append(i)
k=[]
p=list(l)
for i in l:
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        k.append(i)
        p.remove(i)
print(k,'is the list of odd prime numbers')
print(p,'is the list of non prime odd numbers')'''


#x=inp
l=[2,4,13,3,1,5,3]
'''for i in range(len(l)):
    n=l[i]
    j=i-1
    while l[j]>n and j>=0:
        l[j+1]=l[j]
        j-=1
    else:
        l[j+1]=n
        print(l)'''
'''for i in range(len(l)):
    n=l[i]
    j=i-1
    while l[j]<n and j>=0:
        l[j]=l[j]
        j-=1
    else:
        l[j+1]=n
        print(l)'''

l=eval(input('enter:'))
for i in range(len(l)):
    for j in range(len(l)-1-i):
        if l[j+1]<l[j]:
            l[j],l[j+1]=l[j+1],l[j]
        print(l)
    print()
    



























































