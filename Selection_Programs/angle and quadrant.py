#angle and quadrant
a=float(input('enter angle= '))
if a>=0 and a<=90:
    print('quadrant 1')
elif a>=91 and a<=180:
    print('quadrant 2')
elif a>=181 and a<=270:
    print('quadrant 3')
elif a>=271 and a<=360:
    print('quadrant 4')
else:
    print('enter valid angle')