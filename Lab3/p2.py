import random
def quicksort(lista,listb):
    if len(lista)==0 and len(listb)==0:
        return []
    lista+=listb
    p = random.choice(lista)
    front  = [x for x in lista if x > p]
    back = [x for x in lista if x <= p]

    if len(front) <= 1 and len(back) <= 1:
        return front+back
    elif len(front) <= 1:
        if(back[0]==back[1]):
            if (front > back):
                return front + back
            else:
                return back + front
        else:
            backp = random.choice(back)
            back1 = [x for x in back if x > backp]
            back2 = [x for x in back if x <= backp]
            return front+quicksort(back1,back2)
    elif len(back) <= 1:
        if(front[0]==front[1]):
            if(front>back):
                return front+back
            else:
                return back+front
        else:
            frontp = random.choice(front)
            front1 = [x for x in front if x > frontp]
            front2 = [x for x in front if x <= frontp]
            return quicksort(front1,front2)+back
    else:
        frontp = random.choice(front)
        front1 = [x for x in front if x > frontp]
        front2 = [x for x in front if x <= frontp]
        backp = random.choice(back)
        back1 = [x for x in back if x > backp]
        back2 = [x for x in back if x <= backp]
        return quicksort(front1,front2)+[]+quicksort(back1,back2)

print(quicksort([], []))
        
