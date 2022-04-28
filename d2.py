def daily2(lista):
    listaf = []
    sum = 0
    for i in range(len(lista)): 
        lista2 = lista.delete(i)
        for j in lista2:
            sum += j
        listaf.append(sum)
    return listaf