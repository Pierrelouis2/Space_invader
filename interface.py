from tkinter import *

fenetre = Tk()
photo = PhotoImage(file="backgroundimage.png")



label = Label(fenetre, text="Bienvenue dans Space Invader", bg="#d39fce")
label.pack()



bouton = Checkbutton(fenetre, text="Nouveau?")
bouton.pack()

# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

# canvas
canvas = Canvas(fenetre, width=700, height=500, background='yellow').pack(side=TOP, padx=5, pady=5)
#canvas.create_image(0, 0, anchor=NW, image=photo)
Button(fenetre, text ='Niveau précedent').pack(side=LEFT, padx=5, pady=5)
Button(fenetre, text ='Niveau suivant').pack(side=RIGHT, padx=5, pady=5)
#canvas.pack()

class alien():
    canvas.create_rectangle()
#class jeu():

        



fenetre.mainloop()


