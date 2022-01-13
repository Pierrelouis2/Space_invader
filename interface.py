import fonction as fct
from tkinter import *


fen = Tk()

frame1=Frame(fen)
frame1.pack(side=TOP)


#titre + score
score = "Score : 2"
texte = "Bienvenue dans Space Invader                                                                                                                       " + score
label = Label(frame1, text=texte, bg="blue")
label.pack()

# bouton de sortie
bouton=Button(frame1, text="Fermer", command=fen.quit)
bouton.pack()

# canvas
photo = PhotoImage(file="image/grand_background.png")
canvas = Canvas(fen, width=photo.width(), height=photo.height(), background="white")
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

#bouton
Button(frame1, text ='Niveau précedent').pack(side='left', padx=5, pady=5)
Button(frame1, text ='Niveau suivant').pack(side='right', padx=5, pady=5)
"""

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""

#création du monde
monde = fct.Monde(canvas=canvas)


#mouvement du joueur                          
canvas.focus_set()
canvas.bind('<Key>', monde.mouv)

 
 #bouton début de jeu
bouton_jouer = Button(frame1, text="Jouer", command=monde.jouer )
bouton_jouer.pack()
   

#initialisation trajectoire tir
monde.player.trajectoire()

#initialisation mort 
monde.mort()


fen.mainloop()



