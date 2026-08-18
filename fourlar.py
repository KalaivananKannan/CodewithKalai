print("Largest of four numbers")
a = 1
b = 3
c = 2
d = 4
def firlar(a, b, c, d):
    if a >= b and a >= c and a >= d:
        print("a is first largest")
    elif b >= a and b >= c and b >= d:
        print("b is first largest")
    elif c >= a and c >= b and c >= d:
        print("c is first largest")
    else:
        print("d is first largest")
firlar(a, b, c, d)
def second_largest(a, b, c, d):
    if a >= b and a >= c and a >= d:
        largest = a
    elif b >= a and b >= c and b >= d:
        largest = b
    elif c >= a and c >= b and c >= d:
        largest = c
    else:
        largest = d

    if a == largest:
        if b >= c and b >= d:
            second = b
        elif c >= b and c >= d:
            second = c
        else:
            second = d
    elif b == largest:
        if a >= c and a >= d:
            second = a
        elif c >= a and c >= d:
            second = c
        else:
            second = d
    elif c == largest:
        if a >= b and a >= d:
            second = a
        elif b >= a and b >= d:
            second = b
        else:
            second = d
    else:
        if a >= b and a >= c:
            second = a
        elif b >= a and b >= c:
            second = b
        else:
            second = c

    print("First largest:", largest)
    print("Second largest:", second)

second_largest(a, b, c, d)