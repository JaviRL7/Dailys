def daily(lista,k):
    for i in lista:
        for j in lista[:1]:
            if i+j == k:
                return True
    return False