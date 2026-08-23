
def addition_whole(a, b):
    c = ()

    while c != b:
        c = (c,)
        a = (a,)

    return a

def subtraction_whole(a, b):
    c = ()

    while addition_whole(b, c) != a:
        c = (c,)

    return c

def multiplication_whole(a, b):
    c = ()
    d = ()

    if a == ():
        return ()

    while c != b:
        c = (c, )
        d = addition_whole(d, a)
    
    return d

def division_whole(a, b):
    c = ()
    d = ()
    if b == ():
        raise ZeroDivisionError
    
    while not (greater_whole(multiplication_whole(b, c), a) or multiplication_whole(b, c) == a): # while b * c < a
        c = d
        d = (d,)
        if multiplication_whole(d, b) == a:
            print(True)
            return d

    return subtraction_whole(c, ((),))

def greater_whole(a, b): # a > b
    if a == b:
        return False
    
    while a != () and b != ():
        a = subtraction_whole(a, ((),))
        b = subtraction_whole(b, ((),))
    
    if a == ():
        return False
    return True

def normalise_int(a):
    a_pos, a_neg = a

    if a_pos == a_neg:
        return ((), ())
    if a_pos == ():
        return ((), a_neg)
    if a_neg == ():
        return (a_pos, ())

    if greater_whole(a_pos, a_neg):
        return (subtraction_whole(a_pos, a_neg), ())
    
    return ((), subtraction_whole(a_neg, a_pos))

def addition_int(a, b):
    a_pos, a_neg = a
    b_pos, b_neg = b

    return (normalise_int((addition_whole(a_pos, b_pos), addition_whole(a_neg, b_neg))))
    
def subtraction_int(a, b):
    if a == b:
        return ((), ())
    a_pos, a_neg = a
    b_pos, b_neg = b

    return (normalise_int( ( addition_whole(a_pos, b_neg), addition_whole(a_neg, b_pos))))

def multiplication_int(a, b):
    a_pos, a_neg = a
    b_pos, b_neg = b

    if (a_pos == () and a_neg == ()) or (b_pos == () and b_neg == ()):
        return ((), ())

    if (a_pos == ()) ^ (b_pos == ()):
        negative = True
    else:
        negative = False
    
    if a_pos == ():
        a_pos = a_neg
    
    if b_pos == ():
        b_pos = b_neg
    
    c = multiplication_whole(a_pos, b_pos)

    if negative:
        return ( (), c)
    
    return (c, ())

def division_int(a, b):
    a_pos, a_neg = a
    b_pos, b_neg = b

    if b == ((), ()):
        raise ZeroDivisionError
    
    if a == ((), ()):
        return ((), ())
    
    if (a_pos == ()) and (b_pos == ()):
        negative = False
        a = tuple(reversed(a))
        b = tuple(reversed(b))
    elif a_pos == ():
        negative = True
        a = tuple(reversed(a))
    elif b_pos == ():
        negative = True
        b = tuple(reversed(b))
    else:
        negative = False
    
    c = ((), ())
    d = ((), ())

    while greater_int(a, multiplication_int(b, d)):
        c = d
        d = addition_int(d, ( ((),) , ()))

    if multiplication_int(b, d) == a:
        answer = d
    else:
        answer = c
    
    if negative:
        return tuple(reversed(answer))
    
    return normalise_int(answer)

def greater_int(a, b):
    a = normalise_int(a)
    b = normalise_int(b)

    c = subtraction_int(a, b)

    if c == ((), ()):
        return False
    
    c_pos, c_neg = c

    if c_pos == ():
        return False
    
    return True

def modulo_int(a, b):
    return subtraction_int(a, multiplication_int(b, division_int(a, b)))

def gcd_int(a, b):
    while greater_int(b, ((), ())):
        c = modulo_int(a, b)
        a = b
        b = c
    return a

def normalise_rational(a):
    a_denominator, a_numerator = a
    gcd = gcd_int(a_denominator, a_numerator)
    a_denominator = division_int(a_denominator, gcd)
    a_numerator = division_int(a_numerator, gcd)
    return (a_denominator, a_numerator)

