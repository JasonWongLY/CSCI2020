def quicksort(lista,listb):
    if len(lista)<=1 or len(listb)<=1:
        return lista,listb
    else:
        p = random.choice(lst)
        low  = [(x for x in lista if x <  p)or(y for y in listb if y <  p)]
        med  = [(x for x in lista if x ==  p)or(y for y in listb if y==  p)]
        high = [(x for x in lista if x >  p)or(y for y in listb if y >  p)]
        return quicksort(low) + med + quicksort(high)
        
