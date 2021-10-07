def output(x,y):
    i=1
    while i<=x:
        print(y,end='')
        i+=1
while True:
    x = input('Please input an integer : ')
    if int(x)<1:
        break
    y=input("Please input the string : ")
    n=int(x)
    i=1
    while i<=n:
        output(n-i,' '*len(y))
        output(i,y)
        output(i-1,y)
        i+=1
        print()
print('Program ends.')