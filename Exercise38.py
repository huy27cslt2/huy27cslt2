a=str(input("Enter month:"))
if (a=='January') or (a=="March") or (a=="May") or (a=='July') or (a=='August') or (a=='October') or (a=='December'):
    print (a,"has 31 days")
elif a=="Febuary":
    print(a,"has 28 or 29 days")
else:
    print(a,'has 30 days')