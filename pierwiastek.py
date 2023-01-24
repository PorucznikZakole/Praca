x = float(input("podaj liczbe "))
eps = float(input("podaj przyblizenie "))
def pierwiastek(x, eps):
    a = 0
    b = x
    while abs(b-a)>eps:
        c=(a+b)/2
        if x<c*c:
            b=c
        else:
            a=c
    return c
print(pierwiastek(x, eps))

