def B(x, binario=""):
    if x == 0:
        if binario.count("0") % 2 != 0:
            return [binario]
        else:
            return []
    else:
        return (B(x - 1, binario + "0") + B(x - 1, binario + "1"))

print(B(4))