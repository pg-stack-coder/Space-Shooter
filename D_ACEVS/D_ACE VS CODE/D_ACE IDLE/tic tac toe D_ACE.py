q=[[' ' for j in range(3)]for i in range(3)]
d=0
for i in q:
    print(i)
while True:
    if d%2==0:
        b=int(input('player 1:enter the column:'))
        a=int(input('player 1:enter the row:'))
        q[a-1][b-1]='x'
    else:
        b=int(input('player 2:enter the column:'))
        a=int(input('player 2:enter the row:'))
        q[a-1][b-1]='o'
    d+=1
    for i in q:
        print(i)
    
   
            
    
    

    
    
