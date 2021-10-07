def checking(x):
    x=x.lower()
    y=x[::-1]
    if x==y:
        return True
    else:
        return False


x=input('Please input a palindrome: ')
while True :
    if checking(x)==True:
        if x.isdigit()==True:
            print('No BRIBING as I am loyal to the King!: ',end='')
        else:
            print('Welcome to the wonderland!')
            break
    else:
        print('I do not understand what you mean! Say again: ',end='')

    x=input()