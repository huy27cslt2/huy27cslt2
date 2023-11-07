a=int(input('Enter human years:'))
if (a<=2) and (a>=0):
    b=a*10.5
    print(' Dog years:',b)
elif a>2:
    b=2*10.5+(a-2)*4
    print(' Dog years:',b)
else:
    print(' Error!')