import pickle

global contents

def load_data(file):
    global contents
    f=open(file,"rb")
    contents=pickle.load(f)
    return contents

def most_follower(dictionary):
    result=[]
    for x in dictionary:
        if len(dictionary[x])>99:
            result.append(x)
    return result

def update():
    global contents
    contents['William Smith'].append('Lorna Carrico')
    contents['Anne Smelcer']=['Christine Phillips', 'Charles Mason', 'Daisy Middleton']
    contents.pop('Mildred Jones')
    for x in contents:
        for i in range(len(x)):
            if x[i]=='Mildred Jones':
                x.pop(i)

def get_num_of_followers():
    global contents
    result_key=[]
    result_value=[]
    for x in contents:
        if len(contents[x])>1:
            result_key.append(x)
            result_value.append(len(contents[x]))
    final=dict.fromkeys(result_key,result_value)
    return final

#load_data('followers.pydata')
#get_num_of_followers()
