#number with highest no. of decimal numbers
l=[]
m=0
for n in range (2,1000):
    R=[];Q=[];r=.1
    while r not in R:
        R.append(int(r))
        Q.append(int(r*10//n))
        r=r*10%n
        if r==0:
            break
    else:
        w=R.index(r)
        Q=Q[w:]
        if len(Q)>len(l):
            l=list(Q)
            m=n
print(len(l))
for i in l:
    print(i,end='')
print()
print(m)
