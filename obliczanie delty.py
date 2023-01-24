import math
print("obliczanie pierwiastkow rownania kwadratowego")

a = int(input("podaj wartosc a: "))
b = int(input("podaj wartosc b: "))
c = int(input("podaj wartosc c: "))

delta = (b * b) - (4 * a * c)

print(delta)
if delta > 0:
    x1 =-b-math.sqrt(delta)/(2*a)
    x2 = -b + math.sqrt(delta) / (2 * a)

    print("x1= ", x1)    
    print("x2= ", x2)    

else:
    if delta == 0:
       x=-b/(2*a) 
       print("x= ", x)
    else:
        print("brak miejsc zerowych")
