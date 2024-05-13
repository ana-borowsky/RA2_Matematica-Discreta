def B(x):
    if x == 2 or x == 3:
        return True
    elif x % 2 == 0:
        return B(x // 2)
    elif x % 3 == 0:
        return B(x // 3)
    else:
        return False


testes = [6, 9, 16, 21, 26, 54, 72, 218]
for teste in testes:
    if B(teste):
        print(f'{teste} Pertence')
    else:
        print(f'{teste} Não pertence')