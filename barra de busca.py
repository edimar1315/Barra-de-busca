
#Criando_Barra_ de_busca - usando Tkinter Python https://www.linkedin.com/in/edimar-barbosa-da-silva-932a4367/

from tkinter import *
import webbrowser

win = Tk()
win.title("BARRA DE PESQUISA")


def Search():
    url = Entry.get()
    webbrowser.open(url)


label1 = Label(win, text="Insira o URL Aqui:", font=("arial", 10, "bold"))
label1.grid(row=0, column=0)

entry = Entry(win, width=80)
entry.grid(row=0, column=1)

button = Button(win, text="Search", command=Search)
button.grid(row=1, column=0, pady=10)

win.mainloop()
