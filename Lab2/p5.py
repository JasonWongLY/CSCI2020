def count_alphabet(test_string):
    number=0
    for i in test_string:
        if i.isalpha()==True:
            number+=1
    return number

def hk_capitalization(test_string):
    ans=''
    for i in test_string:
        if i=='h' or i=='k':
            ans+=i.upper()
        else:
            ans+=i
    return ans

def concat(test_string, new_string):
    ans=test_string+new_string
    return ans

def search(test_string, sub):
    return test_string.rfind(sub)

def letter_count(test_string):
    test_string_lower=test_string.lower()
    i=0
    j=0
    alpha=[]
    number=[]
    while i<26:
        alpha.append(chr(ord('a') + i))
        number.append(test_string_lower.count(chr(ord('a') + i)))
        i+=1
    ans_alpha=[]
    ans_number=[]
    while j<26:
        if number[j] !=0:
            ans_alpha.append(alpha[j])
            ans_number.append(number[j])
        j+=1
    ans=zip(ans_alpha,ans_number)
    return list(ans)