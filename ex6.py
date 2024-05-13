import re
regex = "a\((.*)\)c"

def D(x):
    if x == 'a' or x == 'b' or x == 'c':
        return True

    m = re.match(regex, x)
    return D(m.groups()[0]) if m else False

testes = ['a(b)c', 'a(a(b)c)c', 'a(abc)c', 'a(a(a(a)c)c)c', 'a(aacc)c'] 
for teste in testes: 
    print(f'{teste} {D(teste)}')