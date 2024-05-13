def Rotina(L, j):
    if j == 1:
        return L
    else:
        maior_numero = 0
        for i in range(0, j):
            if L[i] > maior_numero:
                maior_numero = L[i]
                indice = i
        temp = L[indice]
        L[indice] = L[j-1]
        L[j-1] = temp
        print(L)
        return Rotina(L, j - 1)

L = [3, 7, 4, 2, 6 ]
print(Rotina(L, 5))