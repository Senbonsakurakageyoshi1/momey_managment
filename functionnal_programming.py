def fact(n):
    if n<=1:
        return int(1)
    else :
        return int(fact(n-1)*n)

print(fact(5))