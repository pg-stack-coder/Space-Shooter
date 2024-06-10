'''n=int(input('enter the number:'))
for i in range(1,n//2+1):
    if n%i==0:
        break
else:
    print('it is a prime number')
if i !=0:
    print('it is not a prime number')'''

'''n=int(input('enter the number:'))
sum=0
for i in range(1,n+1):
    if n%i==0:
       print(i)
       sum+=i
print(sum,'is the sum of the factors')'''

'''print('this program finds the odd factors')
n=int(input('enter the number:'))
sum=0
for i in range(1,n+1):
    if n%i==0 and i%2!=0:
       print(i)
if 
    print('there is no odd factor')'''

'''n=int(input('enter the number:'))
sum=0
tot=0
for i in range(1,n+1):
    print(i)
    sum+=i
    tot+=sum    
print(tot, 'is the total')'''
while True:
    a=int(input('enter the from number:'))
    b=int(input('enter the to number:'))
    sum=0
    c=0
    if a==1:
        a+=1
    for i in range(a,b+1):
        for t in range(2,i//2+1):
            if i%t==0:
               break
        else:
            print(i,end=',')
            sum+=i
            c+=1
    print('are the prime numbers')
    print('\n',c,'is the number of prime numbers')
    print(sum,'is the sum of the prime numbers')
    s=input('Do you want to continue Y or N')
    if s!='y':
        break
