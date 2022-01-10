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















#Tire un projectile 
""" global liste_projectile
liste_projectile =[]
def tir(event) :
    global canon
    xp1 = canvas.coords(player.obj)[0] +10
    xp2 = canvas.coords(player.obj)[2] -10
    yp1 = 320
    yp2 = 350
    liste_projectile.append(canvas.create_rectangle(xp1,yp1,xp2,yp2,fill="green"))
canvas.bind_all('<space>', tir) """
#mouvement des tirs

def trajectoire() :
    global liste_projectile
    
    for i in liste_projectile :
        
        if canvas.coords(i)[3] > 5 :
            canvas.move(i,0,-10)
            
        else :
            canvas.delete(i) 
            liste_projectile.pop(liste_projectile.index(i))
    fen.after(100,trajectoire)

fen.mainloop()



