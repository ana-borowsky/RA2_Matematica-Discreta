def C(x):
    if x == 1:
        return "a"
    elif x == 2:
        return "b"
    else:
        return C(x - 2) + C(x - 1)
    
    
print(f'{C(4).count("a")}a + {C(4).count("b")}b')