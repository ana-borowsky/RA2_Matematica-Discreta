
def P(x):
    if x == 0:
        return 50000
    else:
        return P(x - 1) * 3

print(P(3))