#write a program to calculate compound interest
p=float(input('enter principal: '))
r=float(input('enter rate: '))
t=float(input('enter time: '))
a=p*(1+(1/r))**t
cp=a-p
print('compound interest= ',cp)
print('amount= ',a)