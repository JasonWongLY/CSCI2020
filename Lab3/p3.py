import pickle

global contents

def load_data(file):
    global contents
    try:
        f=open(file,"rb")
        contents=pickle.load(f)
        return contents
    except IOError:
        print("ERROR: Target file does NOT exist!")
        return {}


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
   # for x in contents:
    #    for i in range(len(x)):
    #        if x[i]=='Mildred Jones':
    #            x.pop(i)
    for x in contents:
        for y in contents[x]:
            if y=='Mildred Jones':
                contents[x].pop(contents[x].index(y))
    try:
        createFile=open("follower-updated.pydata","wb+")
        pickle.dump(contents,createFile)
    except IOError:
        print("This message should not show")

def get_num_of_followers():
    #result_key=[]
    #result_value=[]
    #for x in contents:
     #   if len(contents[x])>1:
      #      result_key.append(x)
       #     result_value.append(len(contents[x]))
    #final=dict.fromkeys(result_key,result_value)
    try:
        f=open("follower-updated.pydata","rb")
        contents_updated=pickle.load(f)

        dict = {}
        for x in contents_updated:
            count = 0
            for y in contents_updated[x]:
                if len(contents_updated[y]) > 1:
                    count += 1
            dict[x] = count
    except IOError:
        print("ERROR: Target file does NOT exist!")
    return dict


