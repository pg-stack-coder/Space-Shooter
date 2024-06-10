d={'martin':'12345','luther':'67890','king':'13579'}
ask=input('Enter whose number you want to change:')
if ask in d.keys():
    change=input('Enter the changed number:')
    d[ask]=change
    print(f'The modified list is {d}')
else:print(f'Sorry {ask} not entered previously')