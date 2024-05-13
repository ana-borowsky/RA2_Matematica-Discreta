def B(x):
    if x >= 2:
        return B(x - 1) + x**2
    else:
        return 1

print(B(3))