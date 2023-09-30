l=['kite','83','?','62','@','rack']
v=input('enter value to search:')
if v in l:
    i=l.index(v)+1
    print('found at:',i)
else:
    print('not found')