from tkinter import *


fenetre = Tk()

label = Label(fenetre, text="Bienvenue dans Space Invader", bg="#d39fce")
label.pack()



bouton = Checkbutton(fenetre, text="Nouveau?")
bouton.pack()

# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

# canvas
canvas = Canvas(fenetre, width=700, height=500, background='yellow')
canvas.pack()

#class jeu():

 #   def __init__(self) :
        



fenetre.mainloop()