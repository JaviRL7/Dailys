def daily(lista,k):
    for i in lista:
        for j in lista[:1]:
            if i+j == k and i is not j:
                return True
    return False