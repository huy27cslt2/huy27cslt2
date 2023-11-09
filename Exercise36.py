a=input('Enter a letter of the alphabet:')
if a.isalpha() and len(a)==1 :
    if a in {'a', 'e', 'i', 'o', 'u'}:
        print(a,"is a vowel")
    elif a=='y':
        print(a,"sometimes is a vowel, and sometimes is a consonant")    
    else:
        print(a,"is a consonant")
else :
    print('Error!')
