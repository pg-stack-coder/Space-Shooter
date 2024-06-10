'''x=input('enter the word:')
for i in range(len(x)):
    for j in range(len(x),i+1,-1):
        k=x[i:j]
        if k[:]==k[::-1]:
            print(k)'''

'''a=input('Enter the word:')
b=input('Enter the word to be changed:')
c=input('Enter the change:')
if b in a:
    a=a.replace(b,c)
    print(a)
else:
    print('change not in word')'''

'''a=input('enter:')
t=a.upper()
s=a.lower()
d=a.capitalize()
f=a.title()
b=input('what do want to count:')
g=a.count(b)
print('upper',t,'lower',s,'capitalize',d,'title',f,'count',g,sep='\n')
h=input('what do want to find:')
j=a.find(h)
k=a.index(h)
print('find',j)
print('index',k)
m=input('enter what to cut from right:')
n=input('enter what to cut from left:')
v=input('enter what to cut from right and left:')
c=a.rstrip(m)
x=a.lstrip(n)
z=a.strip(v)
q=input('enter what to split:')
w=a.split(q)
r=input('enter what to partition:')
e=a.partition(r)
y=q.join(w)
print('rstrip',c,'lstrip',x,'strip',z,'split',w,'partiton',e,'join',y,sep='\n')'''
#Q_1
'''x=input('enter a word:')
j=-1
x=x.lower()
for i in (x):
    if j==1:
        z=i.upper()
    else:
        z=i
    j*=-1
    print(z,end='')'''

#Q_4
'''a=input('Enter the address:')
c=0
for i in (a):
    if i.isdigit():
        print(i,end='')
        c+=1
    if c==6:
        break'''
#Q_3
'''d=input('enter anything:')
a='aeiouAEIOU'
b='qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
c='1234567890'
v=0
for i in d:
    for j in a:
        if i==j:
            v+=1
print(v,'is the number of vowels')
v=0
for i in d:
    for j in b:
        if i==j:
            v+=1
print(v,'is the number of consonents')
v=0
for i in d:
    for j in c:
        if i==j:
            v+=1
print(v,'is the number of digits')'''

#Q_2
a=input('enter the word:')
d='AEIOUaeiou'
c=0
for i in range(len(a)):
    for j in range(len(d)):
        b=a[i:j]
        for k in (b):
            for p in d:
                if k==p:
                    
                        























