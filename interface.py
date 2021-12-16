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
canvas = Canvas(fenetre, width=photo.width(), height=photo.height(), background="white")
canvas.create_image(0, 0, anchor=NW, image=photo)
#rectangle=canvas.create_oval(25,50,25,50,fill='red')
Button(fenetre, text ='Niveau précedent').pack(side='left', padx=5, pady=5)
Button(fenetre, text ='Niveau suivant').pack(side='right', padx=5, pady=5)
canvas.pack()

#class alien():
   # def __init__(self):
    #   self.create_rectangle()
#class jeu():

        



fenetre.mainloop()


