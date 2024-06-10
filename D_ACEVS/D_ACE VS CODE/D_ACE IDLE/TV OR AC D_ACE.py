'''x=int(input('enter a three digit number:'))
y=x//100
z=x//10-(y*10)
v=x-(y*100)-(z*10)


if y>=z>=v:
    print(y*100+z*10+v,'is the greatest number')
elif y>=v>=z:
    print(y*100+v*10+z,'is the greatest number')
elif z>=y>=v:
    print(z*100+y*10+v,'is the greatest number')
elif z>=v>=y:
    print(z*100+v*10+y,'is the greatest number')
elif v>=y>=z:
    print(v*100+y*10+z,'is the greatest number')
elif v>=z>=y:
    print(v*100+z*10+y,'is the greatest number')

if y>=z>=v:
    print(v*100+z*10+y,'is the smallest number')
elif y>=v>=z:
    print(z*100+v*10+y,'is the smallest number')
elif z>=y>=v:
    print(v*100+y*10+z,'is the smallest number')
elif z>=v>=y:
    print(y*100+v*10+z,'is the smallest number')
elif v>=y>=z:
    print(z*100+y*10+v,'is the smallest number')
elif v>=z>=y:
    print(y*100+z*10+v,'is the smallest number')'''

'''x=input('what do you want TV or AC:')

if x=='ac':
    amt=float(input('enter cost of AC:'))
if x=='tv':
    s=float(input('enter cost of TV:'))
if x=='ac':    
    if amt<=30000:
        dis=amt-(5/100*amt)
    elif amt >30000 and amt<=50000:
        dis=amt-(7.5/100*amt)
    elif amt >50000 and amt<=80000:
        dis=amt-(10/100*amt)
    elif amt >80000:
        dis=amt-(12/100*amt)
    print(dis,'is the amount to be paid')

if x=="tv":
    if s<=30000:
        v=s-(2.5/100*s)
    elif s >30000 and s<=50000:
        v=s-(5/100*s)
    elif s >50000 and s<=80000:
        v=s-(7/100*s)
    elif s >80000:
        v=s-(8.5/100*s)
    print(v,'is the amount to be paid')'''


x=int(input('enter no. of days:'))
if x<=10:
    cost=40*x
elif x>10 and x<=30:
    cost=400+(x-10)*60
elif x>30:
    cost=400+1200+(x-30)*80
v=cost/100
if cost>100:
    print('Amount to be paid is',v,'rupees')
else:
    print('Amount to  be paid is',cost,'paise')



















































