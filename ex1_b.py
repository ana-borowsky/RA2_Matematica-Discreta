def A(x):
    if x >= 2:
        return A(x - 1)**(-1)
    else:
        return 2

print(A(4))
