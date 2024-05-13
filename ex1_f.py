def W(x):
    if x == 1:
        return 2
    elif x == 2:
        return 5
    elif x > 2:
        return W(x - 1) * W(x - 2)

print(W(3))