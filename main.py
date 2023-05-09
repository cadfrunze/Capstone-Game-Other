
from tkinter import *
from functionalitati import afisare, learn
import datetime
import pandas

# Configurarea UI + rulare joc

words: dict = afisare()
de_invatat = []


def next_card():
    """Functie pt next card, adica va afisa o noua valoare"""
    global words, timer
    window.after_cancel(timer)
    words = afisare()

    canvas.itemconfig(img_canvas, image=img_front)
    canvas.itemconfig(prim_cuvant, text=f"English")
    canvas.itemconfig(doi_cuvant, text=f"{words['en']}")
    timer = window.after(2000, unknow_card)


def unknow_card():
    """Functie afisare traducere din next_card a cuvantului din engleza"""
    global words, timer
    canvas.itemconfig(img_canvas, image=img_back)
    canvas.itemconfig(prim_cuvant, text="Romana")
    canvas.itemconfig(doi_cuvant, text=f"{words['ro']}")


def cunoastere():
    """Functie pt butonul 'cunosc'"""
    learn.remove(words)
    next_card()

def nu_cunoaste():
    """Functie pt butonul 'nu cunosc'"""
    global de_invatat
    de_invatat.append(words)
    next_card()

# UI
window = Tk()
window.title('Flasy')
window.config(padx=20, pady=20)

timer = window.after(2000, unknow_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
img_front = PhotoImage(file='./images/card_front.png')
img_back = PhotoImage(file='./images/card_back.png')
know_img = PhotoImage(file='./images/right.png')
unknow_img = PhotoImage(file='./images/wrong.png')
img_canvas = canvas.create_image(400, 263, image=img_front)
prim_cuvant = canvas.create_text(400, 163, text='', font=('Ariel', 30, 'italic'))
# canvas.create_text(400, 263, text='inseamna', font=('Ariel', 20))
doi_cuvant = canvas.create_text(400, 363, text='', font=('Ariel', 30, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

know_but = Button(image=know_img, highlightthickness=0, command=cunoastere)
know_but.grid(column=1, row=1)
unknow_but = Button(image=unknow_img, highlightthickness=0, command=nu_cunoaste)
unknow_but.grid(column=0, row=1)

next_card()

window.mainloop()

# Dupa inchiderea programului

all_data = {
    str(datetime.datetime.now()): de_invatat,
}
try:
    file = open('./data/de_invatat.csv', 'r')
    file.close()
except FileNotFoundError:
    data = pandas.DataFrame(all_data)
    data.to_csv('./data/de_invatat.csv')
else:
    data = pandas.read_csv('./data/de_invatat.csv')
    dictionar = data.to_dict(orient='list')
    dictionar.update(all_data)
    print(dictionar)


    # second_data = pandas.DataFrame(dictionar)

