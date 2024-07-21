#write a program to calculate compound interest and final amount
p= float(input('enter principal: '))
r= float(input('enter rate: '))
t= float(input('enter time: '))
n= float(input('enter number of periods: '))
a= p*(1+r/n)**(n*t)
cp= a-p
print('compound interest= ', cp)
print('amount= ',a)