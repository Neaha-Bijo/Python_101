#merit awarding
m=float(input('enter marks= '))
if m>=0 and m<=60:
    print('regular')
elif m>=61 and m<=89:
    print('merit')
elif m>=90 and m<=100:
    print('distinction')
else:
    print('invalid')