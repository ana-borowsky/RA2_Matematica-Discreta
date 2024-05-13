def D(x):
    if x == 1:
        return 3
    elif x == 2:
        return 5
    elif x > 2:
        return (x - 1) * D(x - 1) + (x - 2) * D(x - 2)

print(D(4))
