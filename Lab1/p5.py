import getpass

secret_input=getpass.getpass('Please input goal posts:')
inputS=secret_input.rsplit(' ')
numberKick=0
mark=[0,0,0]

if inputS[0]>inputS[1]:
    temp=inputS[0]
    inputS[0]=inputS[1]
    inputS[1]=temp

while numberKick<5 :
    gNumber = input('Player 2 please kick: ')
    gNumber=int(gNumber)
    if gNumber>int(inputS[0]) and gNumber<int(inputS[1]):
        print('Goal!')
        mark[0]+=1
        mark[1]+=1
    elif gNumber==int(inputS[0]) or gNumber==int(inputS[1]):
        print('Top Bin!!!')
        mark[0]+=2
        mark[2]+=1
    else:
        print('You missed!')
    numberKick+=1

print('Finished with',mark[1], end='')
if mark[1]>1:
    print(' goals and {}'.format(mark[2]), end='')
elif mark[1]==1:
    print(' goal and {}'.format(mark[2]), end='')
if mark[2]>1:
    print(' top bins.')
elif mark[2]==1:
    print(' top bin')
print('Your final score is {}.'.format(mark[0]))
print('Program ends.')