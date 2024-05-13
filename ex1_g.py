def T(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 3
    elif x > 3:
        return T(x - 1) + 2 * T(x - 2) + 3 * T(x - 3)

print(T(4))