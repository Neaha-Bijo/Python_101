s=input('Enter string:')
start=int(input('Enter first value/letter of substring:'))
stop=int(input('Enter last value/letter of substring:'))
ss=''
for i in range(start-1,stop):
    ss+=s[i]
print(ss,end='')
