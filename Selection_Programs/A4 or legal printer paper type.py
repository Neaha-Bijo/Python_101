#A4 OR LEGAL PAPER
l=int(input('enter no. of lines to print= '))
ppt=(input('enter printer paper type(A4 OR LEGAL)= '))
if ppt=='A4' or ppt=='a4':
    nop=l//25
    if (l%25)==0:
        print('no of A4 printer paper required= ',nop)
    else:
        print('no of A4 printer paper required= ', nop+1)
elif ppt=='LEGAL' or ppt=='legal':
    nop=l//30
    if (l%30)==0:
        print('no of legal printer paper required= ', nop)
    else:
        print('no of legal printer paper required= ',nop+1)
else:
    print('enter A4 or legal paper type')