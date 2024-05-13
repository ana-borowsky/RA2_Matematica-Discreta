def P(x): 
    if x == 1:
        return 1
    else:
        return x + P(x - 1)

print(P(4))