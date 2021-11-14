import random
def quicksort(lista,listb):
    result=lista+listb
    if len(result)<=1:
        return result
    else:
        piv=random.choice(result)
        result1=[x for x in result if x<piv]
        result2=[x for x in result if x==piv]
        result3=[x for x in result if x>piv]
        return quicksort([],result3)+result2+quicksort(result1,[])
