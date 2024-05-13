def S(x):
    if x >= 2:
        return S(x - 1) + 10
    else:
        return 10

print(S(4))
