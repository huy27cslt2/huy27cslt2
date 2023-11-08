month=input('Enter the month:') 
day=int(input('Enter tha day:'))
if month=="January" and day==1:
    print("New year's day")
elif month=='July' and day==1:
    print('Canada day')
elif month=='December' and day==25:
    print('Christmas day')
else:
    print('The month and day entered do not match a fixed holiday date.')
