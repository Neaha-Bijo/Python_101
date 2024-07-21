#write program to calculate simple interest
p=float(input('enter principal: '))
r=float(input('enter rate: '))
t=float(input('enter time: '))
si=p*r*t/100
a=si+p
print('simple inetrest= ', si)
print('amount= ', a)