x=input('Do you want S.I. OR C.I.')
if x=='si':
    P=float(input('enter the Principal:'))
    T=float(input('enter the Time:'))
    R=float(input('enter the rate of interest:'))
elif x=="ci":
    m=float(input('enter the Principal:'))
    t=float(input('enter the Time:'))
    r=float(input('enter the rate of interest:'))
if x=='si':
    n=(P*R*T)/100
    d=round(P+n,2)
    print(d,'is the required amount')

elif x=='ci':
    c=m*(1+r/100)**t
    f=round(c-m,2)
    print(f,'is the required amt')
