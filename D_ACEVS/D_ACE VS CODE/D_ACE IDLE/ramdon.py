'''import math
a=math.sqrt(25)
print(a)
b=math.ceil(5.5)
print(b)
c=math.floor(5.5)
print(c)
d=math.log10(100)
print(d)
e=math.fabs(-34)
print(e)
f=math.factorial(9)
print(f)'''

'''import random
a=random.random()
print(a)
b=random.randint(12,123)
print(b)
d=random.randrange(10,100,5)
print(d)'''

import random
print('Soldier!! to diffuse a bomb you need to'
      'try and guess a number between 10 and 50.GOOD LUCK')
c=0

s=0

m=random.randint(11,50)
while c!=5:
    if c>=1:
        g=int(input('Wrong guess Try again:'))
    else:
        g=int(input('guess the number:'))
    if g==m:
        print('Victory:)',m)
        break
    else:
        c+=1
if c==5:
    print('BOOOOM:( \nThe number was',m)

'''x='lotus boat is'
c=' god'
print(x[:],x[:10],x+c,x[::-1],x[:3],x[3:],c[:],sep='\n')'''

'''x='IkmjDxavcgeh'
for i in range(0,len(x),2):
    print(x[i])'''

'''x='ymocub ncjaknf ldpor tiut'
print(x,'This becomes',sep='\n')
s=input('press enter')
for i in range(0,len(x),2):
    print(x[i])
print('power of coding')'''

'''x=input('enter the number:')
if x[::-1]==x:
    print('Yes it is a pallindrome')
else:
    print('No it is not a pallindrome')'''
















































