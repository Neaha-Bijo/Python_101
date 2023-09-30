d={}
n=int(input('Enter no of elements:'))
for i in range (n):
    e=input('Enter name of employee:')
    bs=int(input('Enter basic salary:'))
    d[e]=bs
print(d)
print(d.keys())
e=input('Enter name of employee to view:')
print('Basic Salary:',d.get(e))
bs=d[e]
hr=0.3*bs
ca=0.01*bs
pf=0.09*bs
gs=bs+hr+ca-pf
print('House Rent:',hr)
print('Conveyance Allowance:',ca)
print('PF:',pf)
print('Gross Salary:',gs )
 


