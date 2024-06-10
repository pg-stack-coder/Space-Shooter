#Q_1
'''s=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        s+=i
print(s)'''
#Q_2
'''x=int(input('enter a number:'))
for i in range(2,x+1):
    if x%i==0:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            print(i,end=',')'''
#Q_4
'''print('This program finds the LCM of numbers from 1 to 10')
i=11
while True:
    for j in range(1,11):
        if i%j!=0:
            break
    else:
        print(i)
        break
    i+=1'''
        
#Q_5
'''print('this program finds the 100th prime number')
c=0
i=1
while c<100:
    i+=1
    
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        c+=1
print(i,'is the 100th prime number')'''

#Q_7
'''s=0
for i in range(2,101):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        s+=i
print(s,'is the sum of prime numbers below hundred')'''



#Q_9
'''a=int(input('enter the base:'))
b=int(input('enter the exponent:'))
c=pow(a,b);s=0
print(c)
while c!=0:
    m=c%10
    c//=10
    s+=m
print(s,'is the sum of digits')'''  

#Q_3
for i in range(99,10,-1):
    for t in range(99,10,-1):
        a=i*t
        b=a
        r=0
        while a!=0:
            m=a%10
            a=a//10
            r=r*10+m
        if (b)==r:
            print(b)
            break
    break

#Q_6
'''f=0
for i in range(1,101):
    for j in range(1,101):
        c=((i**2)+(j**2))**0.5
        if c>100:
            break
        d=round(c,1)
        if d==c and c<100:
            if i>j:
                f+=1
                print(i,j,c,sep=',')    
print(f,'is the number of triplets')'''

#Q_8
'''i=0
j=0
while True:
    i+=1
    j+=i
    c=0
    for t in range(1,j+1):
        if j%t==0:
            c+=1
    if c==10:
        print(j,'is the number that has exactly 10 divisors')
        break'''


'''n=int(input('enter the to number:'))

for t in range(1,n+1):
    s=0
    k=0
    for i in range(1,t//2+1):
        if t%i==0:
            s+=i
    for j in range(1,s//2+1):
        if s%j==0:
            k+=j
    if t==k and t>=s:
         print(t,s,sep=',')'''













































