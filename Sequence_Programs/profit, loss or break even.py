#profit, loss or break even
cp=float(input('enter cost price= '))
sp=float(input('enter selling price= '))
if sp>cp:
    p= sp-cp
    print('profit')
    print('profit= ',p)
elif sp<cp:
    l=cp-sp
    print('loss')
    print('loss= ',l)
else:
    print('break even')