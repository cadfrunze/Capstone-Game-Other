# Configurarea UI + rulare joc
from tkinter import *
from functionalitati import afisare, learn
import datetime
import pandas
import json as js

words: dict = afisare()

# Date pt salvarea datelor
de_invatat = {
    'en': [],
    'ro': []
}

cunoscut = {
    'en': [],
    'ro': [],
}


# Functionalitatile si configurarea aplicatiei
def nex_card():
    """Functionalitate cunoaste"""
    global words, timer
    window.after_cancel(timer)
    words = afisare()

    canvas.itemconfig(img_canvas, image=img_front)
    canvas.itemconfig(prim_cuvant, text=f"English")
    canvas.itemconfig(doi_cuvant, text=f"{words['en']}")
    timer = window.after(2000, unknow_card)


def unknow_card():
    """Functionalitate nu cunoaste"""
    global words, timer
    canvas.itemconfig(img_canvas, image=img_back)
    canvas.itemconfig(prim_cuvant, text="Romana")
    canvas.itemconfig(doi_cuvant, text=f"{words['ro']}")


def cunoastere():
    """Buton Cunoaste"""
    global cunoscut
    cunoscut['en'].append(words['en'])
    cunoscut['ro'].append(words['ro'])
    learn.remove(words)
    nex_card()


def nu_cunoaste():
    """Buton Nu_cunoaste!"""
    global de_invatat
    de_invatat['en'].append(words['en'])
    de_invatat['ro'].append(words['ro'])
    nex_card()


# GUI
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

nex_card()

window.mainloop()
# Dupa inchidera jocului
# Salvare date
# salvare date de_invatat_csv
try:
    file = open('./data/de_invatat.csv', 'r')
    file.close()
except FileNotFoundError:
    data = pandas.DataFrame(de_invatat)
    data.to_csv('./data/de_invatat.csv')
else:
    data = pandas.read_csv('./data/de_invatat.csv')
    dictionar = data.to_dict()
    dictionar.clear()
    dictionar.update(de_invatat)
    data = pandas.DataFrame(dictionar)
    data.to_csv('./data/de_invatat.csv')
# Salvare date nu_cunoaste.csv
try:
    file = open('./data/cunoaste.csv', 'r')
    file.close()
except FileNotFoundError:
    data_cunoasteCsv_tocsv = pandas.DataFrame(cunoscut)
    data_cunoasteCsv_tocsv.to_csv('./data/cunoaste.csv')
else:
    data_cunoasteCsv = pandas.read_csv('./data/cunoaste.csv')
    data_cunoasteCsv = data_cunoasteCsv.to_dict()
    data_cunoasteCsv.clear()
    data_cunoasteCsv.update(cunoscut)
    data_cunoasteCsv_tocsv = pandas.DataFrame(cunoscut)
    data_cunoasteCsv_tocsv.to_csv('./data/cunoaste.csv')
# Salvare date in foderrul ./history history.json
TIMP_DATA = f'{datetime.datetime.now()}'
data_json = {
    TIMP_DATA: {
        'cunoaste': {
            'en': cunoscut['en'],
            'ro': cunoscut['ro'],
        },
        'nu_cunoaste': {
            'en': de_invatat['en'],
            'ro': de_invatat['ro'],
        }
    }
}

try:
    file = open('./data/history/history.json', 'r')
    file.close()
except FileNotFoundError:
    with open('./data/history/history.json', 'w') as fila:
        js.dump(data_json, fila, indent=2)
else:

    fila = open('./data/history/history.json', 'r')
    data_upload: dict = js.load(fila)
    data_upload.update(data_json)
    fila.close()
    with open('./data/history/history.json', 'w') as upload:
        js.dump(data_upload, upload, indent=2)

# Subiect incheiat!