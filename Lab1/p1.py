i=1
failInput=0
y=[]
number=['first','second','third','fourth','fifth']
def is_integer(n):
    if n.isnumeric()==False:
        return False
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

while i<6:
    print('Please input the ',number[i-1],' number: ',end='')
    x=input()
    if is_integer(x):
        y.append(int(x))
        i+=1
    else:
        print('Your input is not an integer!')
        i+=1
        failInput+=1



average=sum(y)/len(y)
i=1
max=int(average)
'''while i<len(y):
    if average>=y[i]:
        if y[i]>max:
            max=y[i]
            i+=1
        else:
            i+=1
    else:
        i+=1'''

if len(y)<3:
    max1=y.min()
else:
    y.sort(reverse=True)
    max1=y[2]


if max1>max:
    print('The value is ',max1)
    print('Program ends.')
else:
    print('The value is ',max)
    print('Program ends.')
