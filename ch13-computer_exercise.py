def sigma(f,lb,ub):
    """Returns the sum of f(k) as k goes from lb to ub, inclusive"""
    acc = 0
    for k in range(lb,ub+1):
        acc = acc + f(k)
    return acc

def add(n):
    return 1/n

