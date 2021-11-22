class node:
    def __init__(self,val):
        self.value=val
        self.left_tree=None
        self.right_tree=None

def BST(arr):
    if not arr:
        return None
    mid=int((len(arr))/2)
    root=node(arr[mid])
    root.left_tree=BST(arr[:mid])
    root.right_tree=BST(arr[mid+1:])
    return root

def preOrder(node):
    if not node:
        return
    print(node.value)
    preOrder(node.left_tree)
    preOrder(node.right_tree)

global pred
pred=None
def predecessor(nodes,p):
    global pred
    if nodes.value==p:
        temp=nodes
        while nodes.right_tree:
            temp=nodes.right_tree
        pred=temp
        return
    elif nodes.value<p:
        pred=nodes
        if nodes.right_tree is not None:
            predecessor(nodes.right_tree,p)
        else:
            return
    elif nodes.value>p:
        if nodes.left_tree is not None:
            predecessor(nodes.left_tree,p)
        else:
            return

'''class BST:
    def __init__(self):
        self.root=None

    def define(self,arr):
        if not arr:
            return None
        mid = int((len(arr)) / 2)

        self.root = node(arr[mid])
        self.root.left_tree = self.define(arr[:mid])
        self.root.right_tree = self.define(arr[mid + 1:])


    def preOrder(self,node):
        if not node:
            return
        print(node.value,
        self.preOrder(node.left_tree),
        self.preOrder(node.right_tree))'''

result=[]
with open("ds.txt") as file:
    arr=[int(value) for value in file]
arr.sort()
tree=BST(arr)

with open("qs.txt") as q_file:
    qry=[x.replace("qry ","") for x in q_file]


for i in qry:
    pred=None
    predecessor(tree,int(i))
    if not pred:
        result.append("no\n")
    else:
        result.append(str(pred.value)+"\n")

with open("output.txt","a") as output:
    output.writelines(result)
