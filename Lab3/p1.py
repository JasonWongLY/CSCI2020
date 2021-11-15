import string
stringSample = []
number = []
ans_stringSample = []
ans_number = []

def reset():
    stringSample[:] = []
    number [:]= []
    ans_stringSample [:]= []
    ans_number [:]= []

def non_unique(xlist):
    reset()
    for row in xlist:
        for elem in row:
            if stringSample.count(elem)==0:
                stringSample.append(elem)
                number.append(1)
            else:
                number[stringSample.index(elem)]+=1

    for i in range(len(number)):
        if number[i]>2:
            ans_stringSample.append(stringSample[i])
            ans_number.append(number[i])


    result=dict(zip(ans_stringSample,ans_number))
    return result

