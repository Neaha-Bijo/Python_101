w=input('Enter word:')
v=0
c=0
if w.isalpha():
    wl=w.lower()
    for i in wl:
        if i in ['a','e','i','o','u']:
            v+=1
        else:
            c+=1
else:
    print('Enter a word')
print('No. of vowels:',v)
print('No. of consonants:',c)
