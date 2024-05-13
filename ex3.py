def A(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        return A(x - 3) or A(x // 2)

testes = [6, 7, 19, 12]
for teste in testes:
    if A(teste):
        print(f'{teste} Pertence')
    else:
        print(f'{teste} Não pertence')