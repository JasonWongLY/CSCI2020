import string
alpha=list(string.ascii_lowercase)
number=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ans_alpha=[]
ans_number=[]
def non_unique(xlist):
    for row in xlist:
        for elem in row:
            number[alpha.index(elem)]+=1
    j=0
    while j<26:
        if number[j]>1:
            ans_number.append(number[j])
            ans_alpha.append(alpha[j])
        j+=1
    ans=list(zip(ans_alpha,ans_number))
    print(ans)

non_unique([['a','a'], ['c','e','e','f'], ['d','a'],['e','f']])
