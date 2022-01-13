import fonction as fct
from tkinter import *


fen = Tk()

frame1=Frame(fen)
frame1.pack(side=TOP)


#titre + score
score = 0
vie=3
texte = StringVar()
texte.set("Bienvenue dans Space Invader                              Vie : " +str(vie)+"                                              Score : "+str(score))
label = Label(frame1, textvariable=texte, bg="white")
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
monde = fct.Monde(canvas=canvas, texte=texte)
score = monde.var


#mouvement du joueur                          
canvas.focus_set()
canvas.bind('<Key>', monde.mouv)

 
 #bouton début de jeu
bouton_jouer = Button(frame1, text="Jouer", command=monde.jouer )
bouton_jouer.pack()
   
#initialisation mvt enemy
monde.path_monster()

#initialisation trajectoire tir
monde.player.trajectoire()

#initialisation tir enemy
monde.tir_enemy_monde()


#initialisation mort 
monde.mort_enemy()
monde.mort_player()

fen.mainloop()



