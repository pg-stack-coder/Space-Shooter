'''x=int(input('enter any number'))
if x%2==0:
    print('it is an even number')
else:
    print('it is an odd number')'''


'''x=int(input('enter any number'))
if x%2==0:
    print(x**2)
else:
    print(x/2)'''
    

'''x=int(input('enter any number between 1,7:'))
if x==1:
    print("monday")
elif x==2:
    print("tuesday")
elif x==3:
    print("wednesday")
elif x==4:
    print('thursday')
elif x==5:
    print('friday')
elif x==6:
    print('saturday')
elif x==7:
    print('sunday')
else:
    print("check entered number again and enter number between 1,7")'''

'''x=int(input('enter your ut 1 HV marks:'))
if x<25 and x>=23:
    print('O grade')
elif x<23 and x>=20:
    print('A grade')
elif x<20 and x>=16:
    print('B grade')
elif x<16 and x>=12:
    print('C grade')
elif x>12 and x>=9:
    print('D grade')
else:
    print('F grade')'''


units=float(input('enter number of units consumed:'))
if units<=50:
    cost=0
elif units>50 and units<=200:
    cost=units-50
elif units>200 and units<=300:
    cost=150+(units-200)*3
elif units>300 and units<=500:
    cost=150+300+(units-300)*5
elif units>500 and units<=600:
    cost=450+1000+(units-500)*7
elif units>600:
    cost=1450+700+(units-600)*10
print('your electricity bill is :',cost)


























          
