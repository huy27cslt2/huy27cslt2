a=int(input('Nhap so nam con nguoi:'))
if (a<=2) and (a>=0):
    b=a*10,5
elif a>2:
    b=2*10,5+(a-2)*4
else:
    print('Khong hop le!')
print('So nam con cho:',b)