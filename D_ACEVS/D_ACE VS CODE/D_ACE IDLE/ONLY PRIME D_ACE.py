for i in range (2,1000):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        print(i,end=',')
