import logic
import math

def peano_readable_whole(a):
    b = 0
    
    while a != ():
        a = logic.subtraction_whole(a, ((),))
        b += 1

    return b

def readable_peano_whole(a):
    b = ()

    while a > 0:
        a -= 1
        b = (b,)

    return b

def peano_readable_int(a):
    pos, neg = a
    b = peano_readable_whole(pos)
    c = peano_readable_whole(neg)

    return b - c

def readable_peano_int(a):
    if a == 0:
        return ((), ())
    
    if a < 0:
        return ((), readable_peano_whole(a * -1))
    
    return (readable_peano_whole(a), ())

def peano_readable_rational(a):
    denominator, numerator = a
    denominator = peano_readable_int(denominator)
    numerator = peano_readable_int(numerator)

    return denominator / numerator

def readable_peano_rational(a):
    if "." in str(a):
        b = len(str(a).split(".")[1])
    else:
        b = 0
    
    n = 10 ** b
    c = int(a * n)
    d = math.gcd(c, n)

    c = int(c / d)
    n = int(n / d)

    print(f"{c} / {n}")
    return ( readable_peano_int(c), readable_peano_int(n))
