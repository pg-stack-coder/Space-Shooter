#Quetsion 4 str to dict with value as count and key as the str items
##c='we3resssssource';d={};l=list(c)
##for i in range(len(c)):
##    d[c[i]]=l.count(c[i])
##print(d)

##import json
##d={'w': 1, 'e': 3, '3': 1, 'r': 2, 's': 5, 'o': 1, 'u': 1, 'c': 1}
##print(json.dumps(d,indent=5))
##d={'w': 1, 'e': 3, '3': 1, 'r': 2, 's': 5, 'o': 1, 'u': 1, 'c': 1}
##d.setdefault('w',5)
##l='debajyotisahu'
##di={}
##di=di.fromkeys(l,100)
##w=d.pop(23,'not my fault its yours check index')
##print(w) 
##print(di)
##d1={1:'1',2:'2',3:'3'}
##d2={1:'1',4:'4',5:'5',2:'2',3:'3'}
##for i in d1.keys():
##    if i in d2:
##        print(i)

d1={1:'1',2:'2',3:'3'}
d2={1:'1',4:'1',5:'5',2:'2',3:'3','dic':{1:'1',2:'2',3:'3'}}
##for i in d1:
##    if d1[i] == d2[i]:continue
##    else: print('d1 not in d2');break
##else: print('d1 in d2')

'''k=d2.values();j=list(k);t=False

for i in k:
    if j.count(i)>1:
        print(j.count(i),'keys have same values')
        t=True
if t==False:
    print('no keys have same values')'''

##d1={'a':[1,2,3],'b':[4,5,6]};d3={}
##for i in d1.keys(): d3[i]=sum(d1[i])
##print(d3)

d2={1:'1',4:'4',5:'5',2:'2',3:'3'}
print(dict(zip(d2.values(),d2.keys())))

##d={}
##for i in range(2):
##    m=input('enter the name:');k=eval(input('enter the roll no.,marks,class:'));d[m]=k
##print('created dictionary:',d)

x={'january':31,'february':28,'march':31,'april':30,'may':31,'june':30,'july':31,\
   'august':31,'september':30,'october':31,'november':30,'december':31}
#b=input('enter the month:');print(x[b],'is the number of days in the month')
#print(sorted(x.keys()))
##for i in x:
##    if x[i]==31:print(i,end=',')
##c=sorted(list(x.values()));new={}
##for i in c:
##    for j in x:
##        if i==x[j]:
##            new[j]=i
##print(new)

'''To change nested dict value'''
##c={5:'5',6:'2',8:'3','dic':{1:'1',2:'2',3:'3'}};ans=0
##print(c)
##
##while ans!='n':
##    j=eval(input('enter the key whose value you want to change:'))
##    
##    if j not in c:
##        print('key not in dictionary :')
##    elif j=='dic':
##        l=eval(input('enter the key of nested dictionary:'))
##        k=eval(input('enter the change:'))
##        c['dic'][l]=k
##    else:
##        k=eval(input('enter the change:'))
##        c[j]=k
##    print(c)
##    ans=input('do you want to continue(y/n):')
##    

'''To get key of min val'''
##g={'1':23,'2':32,'3':45,'4':54}
##d=min(g.values())
##for i in g:
##    if g[i]==d:
##        print(i,':',d,sep='')

'''To rename key of a dictionary'''
##g={'1':23,'2':32,'3':45,'4':54}
##print(g)
##l=eval(input('enter the key you want change:'))
##m=eval(input('enter the change:'))
##g[m]=g.pop(l)
##print(g)

'''delete a list of keys'''
##g={'1':23,'2':32,'3':45,'4':54}
##print(g)
##k=eval(input('enter the list of keys you want to delete:'))
##for i in k:
##    g.pop(i)
##print(g)
    
'''To create a dictionary by extracting keys from a dictionary'''
##g={'1':23,'2':32,'3':45,'4':54};m={}
##print(g)
##k=eval(input('enter the list of keys you want in new dictionary:'))
##for i in k:
##    m[i]=g[i]
##print(m)
'''incomplete 8 QUEEN problem'''
##l=[[' 'for i in range(8)]for j in range(8)]
##def matrix(c):
##    for i in c:
##        print(i)
##l[5][6]='Q'
##matrix(l)
##def colm(x):
##    for i in range(8):
##        if l[i][x]=='Q':
##            return False
##    else:
##        return True
##def row(x):
##    for j in range(8):
##        if l[x][j]=='Q':
##            return False
##    else:
##        return True
##def diagonal(x,y):
##    if x>0:
##        for i in range(8-x):
##            if l[i][x]=='Q':
##                x+=1
##                return False
##            else:
##                 x+=1
##        else:return True
##    elif x==0:
##        for i in range(8-y):
##             if l[y][i]=='Q':
##                 y+=1
##                 return False
##             else:
##                 y+=1
##        else:
##            return True


 
        

            
            
            
        

            














    



































