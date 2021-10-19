def check_sublist(list1, d1, d2, d3):
    lista_index=max(d1,d2,d3)
    listb_index=d1*(d2+d3)
    listc_index=d1+d2+d3
    lista=[]
    listb=[]
    listc=[]
    
    for i in list1:
        if i>lista_index:
            lista.append(i)
            
    for j in list1:
        if j>listb_index:
            listb.append(j)
    
    for k in list1:
        if k<listc_index:
            listc.append(k)
    
    return lista, listb, listc