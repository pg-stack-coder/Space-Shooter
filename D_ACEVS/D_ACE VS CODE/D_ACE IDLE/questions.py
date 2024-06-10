#QUESTION 1 1x,2x,3x,4x,5x,6x
'''x=1000
while True:
    x2=x*2;x3=x*3;x4=x*4;x5=x*5;x6=x*6
    s=str(x);s2=str(x2);s3=str(x3);s4=str(x4);s5=str(x5);s6=str(x6)
    l1=list(s);l2=list(s2);l3=list(s3);l4=list(s4);l5=list(s5);l6=list(s6)
    l1.sort();l2.sort();l3.sort();l4.sort();l5.sort();l6.sort()
    if l1==l2==l3==l4==l5==l6:
        print(x,x2,x3,x4,x5,x6,sep='\n')
        break
    else:
        x+=1'''

#QUESTION 2 find luychrel numbers 
'''l=[]
def reverse(x):
    rev=0
    while x!=0:
        y=x%10
        x=x//10
        rev=rev*10+y
    return rev
for i in range(10000):
    x=i
    c=0
    for j in range(50):
        rev=0;a=x
        rev=reverse(x)
        sum=x+rev
        if sum==reverse(sum):
            break     
        else:
            x=sum
            c+=1
    if c==50:
        l.append(i)
        print(i)    
print(len(l),'is the number of lychrel numbers below 10000')'''

#question 3
'''x=int(input('enter a side:'))
n=1;y=1;sign=1;c=0;notc=0
if x%2!=0:
    index1=x//2;index2=x//2
else:
    index1=x//2;index2=x//2-1
l=[['_'for i in range(x)]for j in range(x)]
def matrix(l):
    for i in l:
         print(i)
def prime(v):
    for i in range(2,v//2+1):
        if v%i==0:
            return False
    else:
        return True
while True:
    for i in range(y):
        if n>x**2:
            break
        l[index1][index2]=n
        index2+=sign
        n+=1
    sign*=-1
    if n>x**2:
            break
    for j in range(y):
        if n>x**2:
            break
        l[index1][index2]=n
        index1+=sign
        n+=1
    if n>x**2:
            break
    y+=1
k=j=[]
for i in range(x):
    if prime(l[i][i]):
        k.append(l[i][i])
    else:
        j.append(l[i][i])
for i in range(x):
   if prime(l[i][x-i-1]):
      k.append(l[i][x-i-1])
   else:
      j.append(l[i][x-i-1])
per=len(k)/len(j)*100
print(per)  
print(matrix(l))'''

##permutations with repetition
'''s='1234'
d=set()
for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            for l in range(len(s)):
                d.add(s[i]+s[j]+s[k]+s[l])
print(d,len(d))'''
## x**5==5 digit number
'''a=1;n=0;count=0
while n!=10000000:
    x=a;c=0
    while x!=0:
        m=x%10
        x//=10
        c+=1   
    if round(a**(1/c),6)==int(a**(1/c)):
        count+=1
        print(a,int(a**(1/c)))
    a+=1
    n+=1
print('total numbers :',count)'''
##better one for Q6
num=1
while num!=10000:
    x=1
    while x!=40:
        po=num**x
        if len(str(po))==x:
            print(po,num)
        x+=1
    num+=1
    

    


        
            
    
        
            























                
        
        
        
    
        
    
        

   
    
    
