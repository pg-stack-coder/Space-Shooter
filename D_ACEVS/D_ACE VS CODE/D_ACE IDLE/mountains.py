'''x=int(input('enter the number: '))
for i in range(1,x+1):
    for t in range(1,i+1):
        print(t,end=' ')
    print()'''

'''x=int(input('enter the number: '))
for i in range(1,x+1):
    for t in range(1,i+1):
        print(i,end=' ')
    print()'''


'''x=int(input('enter the number: '))
for i in range(1,x+1):
    for t in range(1,i+1):
        print('*',end=' ')
    print()
    continue
for i in range(x,0,-1):
    for t in range(i,1,-1):
        print('*',end=' ')
    print()'''

'''x=int(input('enter the number: '))

for i in range(1,x+1):
    for t in range(x,i,-1):
        print(' ',end='')
    print('* '*i,end=' ')
    print()
for h in range(x-1,0,-1):
    for j in range(h,x):
         print(' ',end='')
    print('* '*h,end=' ')
    print()'''
    
'''x=int(input('enter the number:'))
k=0
print(' '*(x)+'*')
for i in range(1,x+1):
    for t in range(x,i,-1):
        print(' ',end='')
    print('* '+' '*(k)+'*',end=' ')
    k+=2
    print()
k-=4
for h in range(x-1,0,-1):
    for j in range(h,x):
        print(' ',end='')
    print('* '+' '*(k)+'*',end=' ')
    k-=2
    print()
print(' '*(x)+'*')'''


x=int(input('enter the number:'))
a=int(input('enter number of horizontal diamonds:'))

k=0
print(' '*(x)+'*')
for i in range(1,x+1):
    for t in range(x,i,-1):
        print(' ',end='')
    print('* '+' '*(k)+'*',end=' ')
    k+=2
    print()
k-=4
for h in range(x-1,0,-1):
    for j in range(h,x):
        
        print(' ',end='')
    print('* '+' '*(k)+'*',end=' ')
    k-=2
    print()
print(' '*(x)+'*')
a-=1



'''x=int(input('enter the number:'))
a=int(input('enter number of horizontal diamonds:'))
b=int(input('enter number of vertical diamonds:'))

print(a*(' '*(x-1)+'*'+' '*(x-1)))
j=1
k=x-2
L=x*1
m=x-1
for i in range(x):
    if x>1:
        print(a*(' '*(x-2)+'*'+' '*j+'*'+' '*(x-2)))
        x-=1
        j+=2

for t in range(1,L-1):
        print(a*(' '*t+'*'+' '*(m)+'*'+' '*t))
        m-=2

print(a*(' '*(L-1)+'*'+' '*(L-1)))'''   





































              
