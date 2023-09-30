#output two roots and type of roots
a=float(input('coefficent of x^2= '))
b=float(input('coefficent of x= '))
c=float(input('constant= '))
d=b**2-4*a*c
r1= (-b + (d)**0.5)/(2*a)
print('root of quadratic equation= ',r1)
r2= (-b - (d)**0.5)/(2*a)
print('root of quadratic equation= ',r2)
if d<0:
    print('unreal roots')
elif d>0:
    print('real and distinct roots')
elif d==0:
    print('equal and real roots')
else:
    print('invalid root')
