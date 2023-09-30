n=int(input('enter no. of number:'))
s=0
for i in range (n):
    num=int(input('enter number:'))
    s+=num
a=s//n
print('sum:',s)
print('average:',a)