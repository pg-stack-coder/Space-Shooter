x=int(input('enter a five digit number :'))
if x==0:
    print('zero')

y=x//10000
c=y
if y==0:
    y=('')
elif y==2:
    y=('twenty ')
elif y==3:
    y=('thirty ')
elif y==4:
    y=('forty ')
elif y==5:
    y=('fifty ')
elif y==6:
    y=('sixty ')
elif y==7:
    y=('seventy ')
elif y==8:
    y=('eighty ')
elif y==9:
    y=('ninety ')

a=x//1000-(c*10)
d=a
if y==1:
   a=('')
if a==0:
    a=('')
elif a==1:
    a=('one thousand')
elif a==2:
    a=('two thousand')
elif a==3:
    a=('three thousand')
elif a==4:
    a=('four thousand')
elif a==5:
    a=('five thousand')
elif a==6:
    a=('six thousand')
elif a==7:
    a=('seven thousand')
elif a==8:
    a=('eight thousand')
elif a==9:
    a=('nine thousand')

if c==1 and d==0:
    y=('ten thousand')
elif c==1 and d==1:
    y=('eleven thousand')
elif c==1 and d==2:
    y=('twelve thousand')
elif c==1 and d==3:
    y=('thirteen thousand')
elif c==1 and d==4:
    y=('fourteen thousand')
elif c==1 and d==5:
    y=('fifteen thousand')
elif c==1 and d==6:
    y=('sixteen thousand')
elif c==1 and d==7:
    y=('seventeen thousand')
elif c==1 and d==8:
    y=('eighteen thousand')
elif c==1 and d==9:
    y=('nineteen thousand')
print(y,a)

v=x//100-(c*100)-(d*10)
b=v
if v==0:
    v=('')
elif v==1:
    v=('one hundred')
elif v==2:
    v=('two hundred')
elif v==3:
    v=('three hundred')
elif v==4:
    v=('four hundred')
elif v==5:
    v=('five hundred')
elif v==6:
    v=('six hundred')
elif v==7:
    v=('seven hundred')
elif v==8:
    v=('eight hundred')
elif v==9:
    v=('nine hundred')

n=x//10-(c*1000)-(d*100)-(b*10)
h=n
if n==0:
    n=('')
elif n==2:
    n=('twenty')
elif n==3:
    n=('thirty')
elif n==4:
    n=('forty')
elif n==5:
    n=('fifty')
elif n==6:
    n=('sixty')
elif n==7:
    n=('seventy')
elif n==8:
    n=('eighty')
elif n==9:
    n=('ninety')

m=x-(c*10000)-(d*1000)-(b*100)-(n*10)
f=m
if s==1:
    b=('')
if b==0:
    b=('')
elif b==1:
    b=('one')
elif b==2:
    b=('two')
elif y==3:
    b=('three')
elif b==4:
    b=('four')
elif b==5:
    b=('five')
elif b==6:
    b=('six')
elif b==7:
    b=('seven')
elif b==8:
    b=('eight')
elif b==9:
    b=('nine')









