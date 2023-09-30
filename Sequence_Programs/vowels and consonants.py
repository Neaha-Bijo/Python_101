#vowel and consonants
ch=input('enter a character= ')
if ch>='A' and ch<='Z' or ch>='a' and ch<='z':
    if(ch=='A' or ch=='a' or
       ch=='E' or ch=='e' or
       ch=='I' or ch=='i' or
       ch=='O' or ch=='o' or
       ch=='U' or ch=='u'):
        print(ch, 'is a vowel')
    else:
        print(ch, 'is a consonant')
else:
    print('invalid character')