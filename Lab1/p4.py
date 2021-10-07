GPA=[['A','A-','B+','B','B-','C+','C','C-','D+','D','F'],[4,3.7,3.3,3,2.7,2.3,2,1.7,1,0]]
cGPA=0
totalCredit=0
while True:
    x=input()
    if x=='exit':
        print('Your GPA: {}.'.format(format))
        break
    y=x.rsplit(', ')
    credit=int(y[1])
    #z=y[0].rsplit()
    if GPA[0].count(y[0])==0:
        print('Wrong input!')
        continue
    if credit<=0:
        print('Wrong input!')
        continue
    cGPA+=GPA[1][GPA[0].index(y[0])]*credit
    totalCredit+=credit
    format="{:.2f}".format(cGPA/totalCredit)
    print('Current GPA:',format)
print('Program ends.')