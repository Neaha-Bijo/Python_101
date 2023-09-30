#Menu program  
print('|            Word Dictionary            |')
print('*****************************************')
print('|                                       |')
print('|                                       |')
print('| 1 - View Word                         |')
print('| 2 - Add new Word                      |')
print('| 3 - Modify word meaning               |')
print('| 4 - Delete word                       |')
print('| 5 - Print words (desc)                |')
print('| 6 - Exit                              |')
print('*****************************************')
   
dc = {'happy':'Cheerful','kind':'Gentle','humane':'Gentle','brave':'Fearless','pale':'faded','intrepid':'Fearless'}
print(dc)
ch=int(input("Enter your choice(1/2/3/4/5/6): "))
   
if ch == 1:
    print(dc)
if ch == 2:
   key = input('Enter the new word:  ')
   name = input('Enter the meaning: ')
   d2 = {key:name}
   #d2.fromkeys('key',[name])
   print(d2)
   dc.update(d2)
   print(dc)
elif ch== 3:
    print(dc.keys())
    md = input('enter word whose meaning is to be modified=')
    wm = input('enter meaning to be modified=')
    dc[md]=wm
    print(dc)
elif ch == 4:
    D = input('Enter word to delete: ')
    if D in dc:
        del dc[D]
        print(dc)
    else:
        print('Word not in dictionary')
elif ch == 5 :
    l=list(dc.items())
    l.sort(reverse=True)
    print("Descending order is",l)
elif ch == 6 :
     print('Exit')
     