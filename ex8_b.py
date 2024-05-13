def B(x):
    if x == 1:
        return 2
    else:
        return B(x - 1) / 2

print(B(2))