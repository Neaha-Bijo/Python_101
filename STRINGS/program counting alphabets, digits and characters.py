w=input('Enter a word:')
a=0
d=0
c=0
for i in w:
    if i.isalnum():
        if i.isalpha():
            a+=1
        elif i.isdigit():
            d+=1
    else:
        c+=1
print('No. of alphabets:',a)
print('No. of digits:',d)
print('No. of others characters:',c)

        
    