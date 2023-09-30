# math calculator
opd1=float(input('enter operand 1= '))
opd2=float(input('enter operand 2= '))
opr=input('enter operand= ')
if opr=='+':
    print('opd1','+','opd2','=',opd1+opd2)
elif opr=='-':
    print('opd1','-','opd2','=',opd1-opd2)
elif opr=='*':
    print('opd1','*','opd2','=',opd1*opd2)
elif opr=='/':
    print('opd1','/','opd2','=',opd1/opd2)
elif opr=='%':                             #shows you remainder
    print('opd1','%','opd2','=',opd1%opd2)
else:
    print('enter valid operator')
