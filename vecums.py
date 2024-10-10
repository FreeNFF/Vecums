import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import datetime

logs = Tk()
logs.title("Vecuma kalkulātors")
logs.geometry("500x650")
logs.configure()

virsraksts = tk.Label(text="Vecuma kalkulātors")
virsraksts.grid(row=0, column=1)

vards_raksts = tk.Label(text='Vārds: ')
vards_raksts.grid(row=1, column=0)
vards_ievade = tk.Entry()
vards_ievade.grid(row=1, column=1)

gads_raksts = tk.Label(text='Gads: ')
gads_raksts.grid(row=2, column=0)
gads_ievade = tk.Entry()
gads_ievade.grid(row=2, column=1)


menesis_raksts = tk.Label(text='Mēnesis: ')
menesis_raksts.grid(row=3, column=0)
menesis_ievade = tk.Entry()
menesis_ievade.grid(row=3, column=1)

diena_raksts = tk.Label(text='Diena: ')
diena_raksts.grid(row=4, column=0)
diena_ievade = tk.Entry()
diena_ievade.grid(row=4, column=1)


def get_info():
    
    vards = vards_ievade.get()
    gads = int(gads_ievade.get())
    menesis = int(menesis_ievade.get())
    diena = int(diena_ievade.get())


    

    dzimsana=datetime.date(gads, menesis, diena)

    today = datetime.date.today()

    if (dzimsana.month, dzimsana.day) > (today.month, today.day):
        today.year =today.year -1

    vecums= today.year - dzimsana.year

    listbox.insert(tk.END, f"Sveicāti {vards}! Jums ir {vecums} gadi.")


    vards_ievade.delete(0, tk.END)
    gads_ievade.delete(0, tk.END)
    menesis_ievade.delete(0, tk.END)
    diena_ievade.delete(0, tk.END)


poga_rekins = tk.Button(logs, text="Aprēķināt vecumu",bd=3, command=get_info)# command=logs.aprekins)
poga_rekins.grid(row=5, column=1)

listbox = tk.Listbox(logs, width=50)
listbox.grid(row=6, column=1)

poga_aizvert = tk.Button(logs, text="Aizvērt", bd=3, command=logs.destroy)
poga_aizvert.grid(row=7, column=1)



mainloop()