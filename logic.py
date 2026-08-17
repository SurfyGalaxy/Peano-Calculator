
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
    a = normalise_int(a)
    b = normalise_int(b)
    a_pos, a_neg = a
    b_pos, b_neg = b

    if (a_pos == () and a_neg == ()) or (b_pos == () and b_neg == ()):
        return ((), ())

    if a_pos == () ^ b_pos == ():
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
    pass

prin()