# Configurarea UI + rulare joc
from tkinter import *

window = Tk()
window.title('Flasy')
window.config(padx=20, pady=20)
canvas = Canvas(width=800, height=526, highlightthickness=0)
img_front = PhotoImage(file='./images/card_front.png')
img_back = PhotoImage(file='./images/card_back.png')
know_img = PhotoImage(file='./images/right.png')
unknow_img = PhotoImage(file='./images/wrong.png')
img_canvas = canvas.create_image(400, 263, image=img_front)
prim_cuvant = canvas.create_text(400, 163, text='title', font=('Ariel', 30, 'italic'))
canvas.create_text(400, 263, text='inseamna', font=('Ariel', 20))
doi_cuvant = canvas.create_text(400, 363, text='cuvant', font=('Ariel', 30, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

know_but = Button(image=know_img, highlightthickness=0)
know_but.grid(column=1, row=1)
unknow_but = Button(image=unknow_img, highlightthickness=0)
unknow_but.grid(column=0, row=1)

def joc():


window.mainloop()
