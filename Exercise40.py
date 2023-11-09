a=float(input('Enter the side of the first triangle:'))
b=float(input('Enter the side of the second triangle:'))
c=float(input('Enter the side of the thirt triangle:'))
if (a+b>c) and (a+c>b) and (b+c>a) and (a>0) and (b>0) and (c>0):
    if (a==c) and (a==b):
        print('Equilateral triangle')
    elif (a==b) or (a==c) or (b==c):
        print('Scalene triangle')
    else:
        print('Isosceles triangle')
