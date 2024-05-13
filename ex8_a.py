def A(x):
    if x == 1:
        return 1
    else:
        return A(x - 1) * 3

print(A(4))