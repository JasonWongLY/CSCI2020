from functools import reduce
vehicle_dict={"Sedan": 1500, "SUV": 2000, "Pickup": 3000, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
a = list(range(1,11))
fruit = [
  {
    "apple": 10,
    "pear": 20,
    "banana": 30,
    "strawberry": 50
  },
  {
    "apple": 12,
    "pear": 5,
    "banana": 20,
    "strawberry": 5
  },
  {
    "apple": 15,
    "pear": 26,
    "banana": 32,
    "strawberry": 8
  },
]

# 1
list1=[x.upper() for x in vehicle_dict if vehicle_dict[x]<=2500]

# 2
list2=[" ".join([str(y)+"*"+str(x)+"="+str(x*y) for y in range(1,x+1)]) for x in range(1,10)]

# 3
list3=list(map(lambda x:x**2, a))

# 4
list4=list(filter(lambda x:x%2==0,a))

# 5
import collections
dict5=dict(reduce(lambda x,y:x+y,map(collections.Counter,fruit)))
