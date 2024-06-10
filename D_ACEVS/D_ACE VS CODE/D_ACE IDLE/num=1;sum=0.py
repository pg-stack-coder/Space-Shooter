'''PROBLEM 1'''
n=int(input('enter the number:'))
sum=0;num=1
while num!=n+1:
    for i in range (1,num+1):
        if num%i==0:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                if num%(i**3)==0:
                    sum+=1
    num+=1
print(sum)

'''PROBLEM 2'''
import random,math
initial=int(input('Enter the initial value:'))
final=int(input('Enter the final value:'))
set=range(initial,final+1)
main_list=[]
pfct=[]
count=0
while len(main_list)<(2**len(set))-1:
    r=random.randint(1,len(set))
    temp=[]
    while len(temp)<r:
        r2=random.choice(set)
        if r2 not in temp:
            temp.append(r2)
    temp.sort()
    if temp not in main_list:
        main_list.append(temp)
for i in main_list:
    mul=1
    for j in i:
        mul*=j
        if math.sqrt(mul)==int(math.sqrt(mul)):
            if mul not in pfct:
                pfct.append(mul)
                count+=1
print(count)