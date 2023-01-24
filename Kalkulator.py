print("Kalkulator")

a = input("Podaj pierwsza liczbe: ")
b = input("Podaj druga liczbe: ")
wynik = 0
print("1 - Dodawanie, 2 - Odejmowanie, 3 - Mnożenie, 4 - Dzielenie, 5 - Potęgowanie")
dzialanie = input("Co zrobić? Podaj cyfrę: ")

if dzialanie == "1":
    wynik = float(a)+float(b)
elif dzialanie == "2":
    wynik = float(a)-float(b)
elif dzialanie == "3":
    wynik = float(a)*float(b)
elif dzialanie == "4":
    wynik = float(a)/float(b)
elif dzialanie == "5":
    wynik = float(a)**float(b)
print(wynik)