from tkinter import *
root = Tk()
root.title("kalkulator")


e = Entry(root, width=30, borderwidth=20)
e.grid(row=0, column=0, columnspan=3, padx=30, pady=30)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

#pierwsza cyfra musi miec dostep za pomoca globl, zeby pozostala niezmienna
def button_dodaj():
    pierwsza_cyfra = e.get()
    global p_cyfra
    global dzialanie
    dzialanie = "plus"
    p_cyfra = int(pierwsza_cyfra)
    e.delete(0, END)    

def button_minus():
    pierwsza_cyfra = e.get()
    global p_cyfra
    global dzialanie
    dzialanie = "minus"
    p_cyfra = int(pierwsza_cyfra)
    e.delete(0, END)

def button_mnoz():
    pierwsza_cyfra = e.get()
    global p_cyfra
    global dzialanie
    dzialanie = "mnozenie"
    p_cyfra = int(pierwsza_cyfra)
    e.delete(0, END)

def button_dziel():
    pierwsza_cyfra = e.get()
    global p_cyfra
    global dzialanie
    dzialanie = "dzielenie"
    p_cyfra = int(pierwsza_cyfra)
    e.delete(0, END)

def button_poteg():        
    pierwsza_cyfra = e.get()
    global p_cyfra
    global dzialanie
    dzialanie = "potega"
    p_cyfra = int(pierwsza_cyfra)
    e.delete(0, END)

def button_wynik():
    d_cyfra = e.get()
    e.delete(0, END)
    if dzialanie == "plus":
        e.insert(0, p_cyfra + int(d_cyfra))
    if dzialanie == "minus":
        e.insert(0, p_cyfra - int(d_cyfra))
    if dzialanie == "mozenie":
        e.insert(0, p_cyfra * int(d_cyfra))    
    if dzialanie == "dzielenie":
        e.insert(0, p_cyfra / int(d_cyfra))
    if dzialanie == "potega":
        e.insert(0, p_cyfra ^ int(d_cyfra))


#czyszczenie wiersza 0
def button_czysc():
    e.delete(0,END)

button_dodaj = Button(root, text="+", padx=60, pady=25, command=button_dodaj)
button_minus = Button(root, text="-", padx=60, pady=25, command=button_minus)
button_mnoz = Button(root, text="*", padx=60, pady=25, command=button_mnoz)
button_dziel = Button(root, text="/", padx=60, pady=25, command=button_dziel)
button_poteg = Button(root, text="^", padx=60, pady=25, command=button_poteg)
button_czysc = Button(root, text="C", fg="red", padx=60, pady=25, command= button_czysc)

#lambda ukrywa wywolanie funkcji
button_1 = Button(root, text="1", padx=60, pady=25, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=60, pady=25, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=60, pady=25, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=60, pady=25, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=60, pady=25, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=60, pady=25, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=60, pady=25, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=60, pady=25, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=60, pady=25, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=60, pady=25, command=lambda: button_click(0))
button_wynik = Button(root, text="=", padx=120, pady=25, command=button_wynik)

#tutaj tylko przypisanie miejsca cyfrom oraz funkcjom
button_dodaj.grid(row=2, column=2)
button_minus.grid(row=2, column=1)
button_mnoz.grid(row=1, column=2)
button_dziel.grid(row=2, column=0)
button_poteg.grid(row=1, column=1)
button_czysc.grid(row=1, column=0)
button_wynik.grid(row=6, column=1, columnspan=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_7.grid(row=5, column=0)
button_8.grid(row=5, column=1)
button_9.grid(row=5, column=2)
button_0.grid(row=6, column=0)

root.mainloop()