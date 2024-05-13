def P(x):
    if x >= 2:
        return (x**2) * P(x - 1) + x - 1
    else:
        return 1

print(P(4))