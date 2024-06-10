# 1.Take input and check if a number is even or odd
'''print('This program checks if it is an even or odd number')
number=int(input('enter a number:'))
if number%2==0:
    print('the number entered is even')
else:
    print('the number is odd')'''
# 2.Take input and check if a number is prime or composite
'''num=int(input('enter a number:'))
for i in range(2,num//2+1):
    if num%i==0:
        print('entered numbered is composite')
        break
else:
    print('number is prime')'''
# 3.Take input and find out the number of digits of a number entered
'''print('This program gives the number of digits')
num=input('enter a number:')
print('number of digits =',len(num))'''
# 4.Take input of amount and find out discount
#    25% if 0-25000
#    35% if 25000-100000
#    50% if 100000+
#    print original price,discount,discounted price
'''amt=int(input('enter the amount:'))
if amt<25000:
    discount=1/4*amt
elif amt>=25000 and amt<100000:
    discount=35/100*amt
elif amt>=100000:
    discount=1/2*amt
dis_price=amt-discount
print('original price:',amt,'discount is:',discount,
      'discounted price:',dis_price,sep='\n')'''
# 5.Enter marks in 5 subjects and calculate percentage,total,average
'''print('This program gives the percentage ,average,total')
l=['maths','physics','chemistry','computer science','english'];sum=0
total=int(input('enter the total marks acquirable:'))
for i in range(5):
    marks=int(input(f'enter your marks in {l[i]}:'))
    sum+=marks
percentage=(sum/total)*100
average=sum/5
print('your total is:',sum,'percentage is:',percentage,'average is:',average,sep='\n')'''
# 6.Print first 10 numbers in fibonacci series and their total
'''print('This program gives the first ten numbers in fibonacci series')
f=0;s=1;sum=1
print(f,s,sep=',',end=',')
for i in range(8):
    t=f+s
    sum+=t
    print(t,end=',')
    f,s=s,t
print('\ntheir total is:',sum)'''
# 7.Take input and check if a number is perfect sq or no
'''print('This program checks for perfect square')
num=int(input('enter the number:'))
for i in range(num//2+1):
    if i**2==num:
        print('number is a perfect square')
        break
    elif (i)**2>num:
        print('number is not a perfect square')
        break'''
# 8.Take input and check if a number or a string is palindrome or no
'''print('This program checks for a palindrome')
x=input('enter:')
if x[::-1]==x:
    print('It is a palindrome')
else:
    print('It is not a palindrome')'''
# 9.Take input of a list and find smallest and largest no in a list without inbuilt functions
'''print('this program finds the smallest and greatest number in a list')
l=eval(input('enter a list:'))
max=min=l[0]
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
print(max,'is the greatest value',min,'is the least value')'''
# 10.Take input and convert temperature  from c-f , f-c and c-k and k-c
'''print('This program is temperature scale converter')
ask=input('enter from what to what conversion c-f/f-c/c-k,k-c:')
val=int(input('enter the value:'))
if ask=='k-c':
    print(val-273.15,'is the Celsius value')
elif ask=='c-k':
    print(val+273.15,'is the Kelvin value')
elif ask=='c-f':
    print((9*val/5)+32,'is the fahrenheit value')
elif ask=='f-c':
    print(5/9*(val-32),'is the Celsius value')'''
# 11.Take input of a list with duplicates and remove duplicates from a list
l=[1,2,3,2,3,2,3,2,34,4,4,4,33]
# l=eval(input('Enter a list:'))

# 12.ATM. Enter amount and it shows no of 2k notes 500 notes 200 notes 100,50,20,10,5,2,1.
'''x=int(input('enter the amount:'))
b=x//2000
y=x%2000
c=y//500
d=y%500
o=d//200
e=d%200
f=e//100
g=e%100
a=g//50
v=g%50
n=v//20
m=v%20
k=m//10
j=m%10
q=j//5
w=j % 5
s=w//2
r=w%2
h=r//1
if b!=0:print(b,'two thousand rupee notes')
if c!=0:print(c,"five hundred rupee notes")
if o!=0:print(o,'two hundred rupee notes')
if f!=0:print(f,'hundred rupee notes')
if a!=0:print(a,'fifty rupee notes')
if n!=0:print(n,'twenty rupee notes')
if k!=0:print(k,'ten rupee notes')
if q!=0:print(q,'five rupee notes')
if s!=0:print(s,'two rupee notes')
if h!=0:print(h,'one rupee notes')'''
# 13.code for insertion sort
'''l=eval(input('enter a list:'))
for i in range(len(l)):
    n=l[i]
    j=i-1
    while l[j]>n and j>=0:
        l[j+1]=l[j]
        j-=1
    else:
        l[j+1]=n
        print(l)'''
# 14.Take input of a string and count number of vowels , consonants, numbers and other symbols in a string .
'''ask=input('enter a string:')
vow='aeiou';con='qwrtypsdfghjklzxcvbnm';num='0987654321'
vowel_count=consonant_count=num_count=0
for i in ask:
    if i in vow:vowel_count+=1
    if i in con:consonant_count+=1
    if i in num:num_count+=1
symbols=len(ask)-(vowel_count+consonant_count+num_count)
print(f'number of vowels is {vowel_count},number of consonants is {consonant_count},numbers are {num_count},number of other symbols is {symbols}')'''
# 15.Take input and find sum of factors of a number
'''num=int(input('enter a number:'))
sum=0
for i in range(1,num+1):
    if num%i==0:
        print(i)
        sum+=i
print(fr'Total of factors is {sum}')'''
# 16.100th prime number
'''count=0;num=2
while True:
    for i in range(2,num//2+1):
        if num%i==0:
            break
    else:
        count+=1
    if count==100:
        break
    num+=1
print(f'The 100th prime number is {num}')'''
# 17.Take input of address and find pin code in a the string(address)
'''ask=input('enter the address:')
num='0987654321'
for  i in ask:
    if i in num:
        print(ask[ask.index(i):ask.index(i)+6],'is the PIN code')
        break'''
# 18.Pythagorean triplets below 50
'''for i in range(1,50):
    for j in range(1,50):
        for k in range(1,50):
            if j**2+k**2==i**2 and j>k:
                print(i,j,k)'''
# 19.sum of all multiples of 3 or 5 below 100
'''sum=0
for i in range(100):
    if i%5==0 or i%3==0:
        sum+=i
print(f'The required sum of numbers:{sum}')'''
# 20.Number divisible by all numbers from 1-10
'''num=100
while True:
    for i in range(1,11):
        if num%i !=0:
            break
    else:
        print(f'The number is:{num}')
        break
    num+=1'''
# 21.Take input of a string and make alternate alphabets in a string capital
'''ask=input('enter a string:')
x=''
for i in range(len(ask)):
    if i%2==0:
        x+=ask[i].upper()
    else:
        x+=ask[i]
print(x)'''
# 22.dict={31:111,22:222,43:333,14:444,25:555} write a python program to find the highest 2 values in this dictionary.

# 23.make a dictionary of some of your friend and phone numbers; ask for name and display number
#  and change number for one friend.
'''d={}
for i in range(3):
    name=input('Enter the name:')
    num=input('Enter the phone number:')
    d[name]=num
print(f'The current list is {d}')
ask=input('Enter whose number you want to change:')
change=input('Enter the changed number:')
d[ask]=change
print(f'The modified list is {d}')'''
# 24.take input of a name and check if he is present in the dictionary created in the previous question or no.
'''d={'martin':'12345','luther':'67890','king':'13579'}
ask=input('Enter whose number you want to change:')
if ask in d.keys():
    print('The member in list previously entered')
else:print(f'Sorry {ask} not entered previously')'''
# 25.a dictionary D1 has values in the form of list of numbers. write a program to create a new dictionary(D2) 
# having same keys as D1 but values as sum of elements.
# example . D1={'A':[1,2,3],'B':[4,5,6]}
# 	  D2={'A':6,'B':15}





# ____________PLEASE SUBMIT THIS BY 4TH OF MARCH (THE BOOK SHOULD BE COVERED)_______________________________________
