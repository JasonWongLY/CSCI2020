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
            return front+quicksort([back[x] for x in range(len(back)) if x < int(len(back)/2)],[back[x] for x in range(len(back)) if x >= int(len(back)/2)])
    elif len(back) <= 1:
        if(front[0]==front[1]):
            if(front>back):
                return front+back
            else:
                return back+front
        else:
            return quicksort([front[x] for x in range(len(front)) if x < int(len(front)/2)],[front[x] for x in range(len(front)) if x >= int(len(front)/2)])+back
    else:
        return quicksort([front[x] for x in range(len(front)) if x < int(len(front)/2)],[front[x] for x in range(len(front)) if x >= int(len(front)/2)])+[]+quicksort([back[x] for x in range(len(back)) if x < int(len(back)/2)],[back[x] for x in range(len(back)) if x >= int(len(back)/2)])

