#selection sort
'''l=list(input('enter a number:'))
for i in range (len(l)):
    small=l[i];pos=i
    for j in range(i,len(l)):
        if l[j]<small:
            small=l[j]
            pos=j
    l.pop(pos)
    l.insert(i,small)
    print(l)'''

#exchange selection sort
'''l=eval(input('enter a list:'))
for i in range (len(l)):
    small=l[i];pos=i
    for j in range(i,len(l)):
        if l[j]<small:
            small=l[j]
            pos=j
    l[i],l[pos]=l[pos],l[i]
    print(l)'''

#insertion sort
l=[2,4,13,3,1,5,3]
'''for i in range(len(l)):
    n=l[i]
    j=i-1
    while l[j]>n and j>=0:
        l[j+1]=l[j]
        j-=1
    else:
        l[j+1]=n
        print(l)'''
'''for i in range(len(l)):
    n=l[i]
    j=i-1
    while l[j]<n and j>=0:
        l[j]=l[j]
        j-=1
    else:
        l[j+1]=n
        print(l)'''

#bubble sort
l=eval(input('enter:'))
for i in range(len(l)):
    f=True
    for j in range(len(l)-1-i):
        if l[j+1]<l[j]:
            f=False
            l[j],l[j+1]=l[j+1],l[j]
    print(l)
    if f:
        break

##x=eval(input('enter list:'))
##for i in len(x):
##    j=i-1
##    if l[i]<l[j]:
##        continue
##    else:
##        break







y=int(input('enter the element you are searching for:'))
end=len(x)
beg=0
while beg!=end:
    mid=(beg+end)//2
    if x[mid]==y:
        break
    elif x[mid]<y:
        beg=mid
    elif x[mid]>y:
        end=mid
print(mid)
    





















        
