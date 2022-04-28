def daily(lista,k):
    for i,m in enumerate(lista):
        for j in lista[:i]:
            if m+j == k and i is not j:
                return True
    return False