'''x=input('enter a sentence:')
s=x.split(' ')
for i in s:
    print(i)'''

a=int(input('enter a number:'))
b='I'
n='IV'
m='V'
c='X'
z='IX'
s='L'
d='XL'
f=a%10
g=a//10
c=a%100
if g==0:
    if f<4:
        print(b*f)
    elif f==4:
        print(n)
    elif f>=5 and f<9:
        j=f-5
        if j<4:
            print(m+(b*j))
    elif f==9:
        print(z)
elif g<4:
    if f<4:
        print((c*g)+(b*f))
    elif f==4:
        print((c*g)+n)
    elif f>=5 and f<9:
        j=f-5
        if j<4:
            print((c*g)+m+(b*j))
    elif f==9:
        print((c*g)+z)
elif g==4:
    if f<4:
        print(d+(b*f))
    elif f==4:
        print(d+n)
    elif f>=5 and f<9:
        j=f-5
        if j<4:
            print(d+m+(b*j))
    elif f==9:
        print(d+z)
elif g>=5:
    g=g-5
    if f<4:
        print(s+(c*g)+(b*f))
    elif f==4:
        print(s+(c*g)+n)
    elif f>=5 and f<9:
        j=f-5
        if j<4:
            print(s+(c*g)+m+(b*j))
    elif f==9:
        print(s+(c*g)+z)
    















        
