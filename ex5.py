def C(x):
    primeiro, *restante = x

    if len(restante) == 0 and primeiro == 'a':
        return True
    if len(restante) == 0 and primeiro == 'b':
        return True

    return C(restante) and restante[-1] == 'b'

testes = ['a' , 'ab' , 'aba' , 'aaab' , 'bbbbb']
for teste in testes: 
    print(f'{teste} {C(list(teste))}')