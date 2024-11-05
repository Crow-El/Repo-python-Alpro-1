def faktorial2(n):
    if n>2:
        return n * faktorial2(n-1)
    return 2

n = 10
faktorial2 = faktorial2(n)
print (f'{n}! = {faktorial2}')