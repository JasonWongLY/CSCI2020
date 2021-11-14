import matplotlib
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
mu = 0
sigma = 1
x = mu + sigma * np.random.randn(10000)

# histogram and line chart here
num_bins=100
n,bins,patches = plt.hist(x,num_bins,density=1/10000,color='green')
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
plt.plot(bins,y,linestyle='dashed',color='red')
plt.savefig('histogram_line.png')
plt.clf()

Colleges = {'New Asia College': 3345, 'United College': 3364,
'Shaw College': 3342, 'Morningside College': 300}

# pie chart
label=[x for x in Colleges]
size=[Colleges[x] for x in Colleges]
separate=[]
for i in range(len(size)):
    if i ==size.index(min(size)):
        separate.append(0.1)
    else:
        separate.append(0)
plt.pie(size,labels=label,autopct='%1.1f%%',explode=separate)
plt.savefig("pie.png")
plt.clf()

# bar chart
plt.bar(np.arange(len(label)),size)
plt.xticks(np.arange(len(label)),label)
plt.xlabel('Colleges')
plt.ylabel('Number of Student')
plt.savefig('bar.png')
