'''x=int(input('enter a number:'))
if int(x**0.5)==x**0.5:
   print("this is a perfect square",x**0.5)
else:
   print('this is not a perfect square')'''


x=int(input('enter a four digit number :'))
if x==0:
    print('zero')
y=x//1000
c=y
if y==0:
    y=('')
elif y==1:
    y=('one thousand')
elif y==2:
    y=('two thousand')
elif y==3:
    y=('three thousand')
elif y==4:
    y=('four thousand')
elif y==5:
    y=('five thousand')
elif y==6:
    y=('six thousand')
elif y==7:
    y=('seven thousand')
elif y==8:
    y=('eight thousand')
elif y==9:
    y=('nine thousand')

a=x//100-(c*10)
d=a
if a==0:
    a=('')
elif a==1:
    a=('one hundred')
elif a==2:
    a=('two hundred')
elif a==3:
    a=('three hundred')
elif a==4:
    a=('four hundred')
elif a==5:
    a=('five hundred')
elif a==6:
    a=('six hundred')
elif a==7:
    a=('seven hundred')
elif a==8:
    a=('eight hundred')
elif a==9:
    a=('nine hundred')

v=x//10-(c*100)-(d*10)
s=v
if v==0:
    v=('')
elif v==2:
    v=('twenty')
elif v==3:
    v=('thirty')
elif v==4:
    v=('forty')
elif v==5:
    v=('fifty')
elif v==6:
    v=('sixty')
elif v==7:
    v=('seventy')
elif v==8:
    v=('eighty')
elif v==9:
    v=('ninety')

b=x-(c*1000)-(d*100)-(s*10)
n=b
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

if s==1 and n==0:
    v=('ten')
elif s==1 and n==1:
    v=('eleven')
elif s==1 and n==2:
    v=('twelve')
elif s==1 and n==3:
    v=('thirteen')
elif s==1 and n==4:
    v=('fourteen')
elif s==1 and n==5:
    v=('fifteen')
elif s==1 and n==6:
    v=('sixteen')
elif s==1 and n==7:
    v=('seventeen')
elif s==1 and n==8:
    v=('eighteen')
elif s==1 and n==9:
    v=('nineteen')
print(y,a,v,b)






























    



