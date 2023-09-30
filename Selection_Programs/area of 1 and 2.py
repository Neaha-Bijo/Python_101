#type of shape
t=int(input('enter type of shape(1 for square and 2 for rectangle)= '))
if t==1:
    s=float(input('enter side lenght= '))
    a=s**2
    print('area= ',a)
elif t==2:
    l=float(input('enter lenght= '))
    b=float(input('enter breadth= '))
    a=l*b
    print('area= ',a)
else:
    print('invalid')