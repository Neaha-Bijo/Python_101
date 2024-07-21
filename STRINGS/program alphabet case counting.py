s=input('Enter word:')
up=0
lp=0
if s.isalpha():
    for i in s:
        if i.isupper():
            up+=1
        elif i.islower():
            lp+=1
else:
    print('Enter alphabets')
print('Total upper cases:',up)
print('Total lower cases:',lp)
