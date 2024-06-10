input('enter the number:'))
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
print(