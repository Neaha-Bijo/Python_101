l=['apple','kite','@','ice','track']
for i in l:
    if i.isalpha():
        v=0
        c=0
        for j in i:
            if j in ['a','e','i','o','u']:
                v+=1
            else:
                c+=1
    print('for element:',i)
    print('No. of vowels:',v)
    print('No. of consonants:',c)
