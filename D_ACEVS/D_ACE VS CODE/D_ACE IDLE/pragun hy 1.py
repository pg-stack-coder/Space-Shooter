i=100
c=0
while (c/i)*100!=99.0:
    i+=1
    n=i
    l=[]
    h=[]
    while n!=0:
        k=n%10
        n//=10
        l.append(k)
        h.append(k)
    h.sort()
    if l==h or l==h[::-1]:
        pass
    else:
        c+=1
print(i)

    
    
    
            
            





























    

