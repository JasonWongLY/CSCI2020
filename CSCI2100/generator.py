import random
with open("1MData.txt","w") as file:
    output=random.sample(range(1,10000000),1000000)
    for i in output:
        file.write(str(i)+"\n")
