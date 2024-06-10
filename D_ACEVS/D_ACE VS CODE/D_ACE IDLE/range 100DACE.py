'''x=int(input('enter the number:'))
sum=0
for i in range(1,x//2+1):
    if x%i==0:
        sum+=i
        print(sum,i)
if sum==x:
     print('yes,the sum of the factors is equal to the number')
else:
     print('no,sum of factors is not equal to the number')'''

'''x=int(input('enter any number:'))   
for i in range(1,x+1):    
    j=i
    s=0
    m=1
    while(j!=0):
        k=j%10
        s+=k
        m*=k
       
        j//=10
    if m+s==i:
        print(i)'''

'''x=int(input('enter any number:'))
for i in range(1,x+1):
    m=i
    k=0
    j=0
    while (m!=0):
        k=m%10
        j+=(k**3)
        m//=10
    if j==i:
        print(i,end=',')'''

'''x=int(input('enter any number:'))
f=0
s=1
sum=0
c=0
#print('0',end=',')
while c!=x:
    t=f+s
    
    for m in range(2,t//2+1):
        if t%m==0:
            break
    else:
        c=t
        c+=1
        print(t,end=',') 
    f,s=s,t'''

'''n=int(input('enter any number:'))
rev=0
c=0
while n!=0:
    m=n%10
    n//=10
    rev=rev*10+m
    c+=1
print(rev,'is the reverse number')
print(c,'is the length of the number')'''


'''n=int(input('enter any number:'))
a=n
r=0
while n!=0:
    m=n%10
    n//=10
    r=r*10+m
if a==r:
    print('the number is a palindrome')
else:
    print('the number is not a palindrome')'''

'''s=0
for i in range(5):
    n=int(input('enter a number:'))
    if i==0:
        max=n;min=n
    elif n>max:
        max=n
    if n<min:
        min=n
    s+=n
avg=s/(i+1)
print(max,'is the maximum value entered',min,'is the minimum value entered')
print(avg,'is the average of the numbers')
print(i+1,'is the number of digits entered')'''


'''x=int(input('enter a number'))
n=int(input('enter a number'))
s=0
f=1
sign=1
for i in range(1,n+1):
    f*=i
    s+=((x**i)/f)*sign
    sign*=-1
print(s)'''



















































































        























