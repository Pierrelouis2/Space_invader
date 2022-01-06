import fonction as fct
from tkinter import *


fen = Tk()

frame1=Frame(fen)
frame1.pack(side=TOP)

#titre + score
score = "2"
texte = "Bienvenue dans Space Invader" + score
label = Label(fen, text=texte, bg="#d39fce")
label.pack()

# bouton de sortie
bouton=Button(fen, text="Fermer", command=fen.quit)
bouton.pack()


# canvas
photo = PhotoImage(file="image/grand_background.png")
canvas = Canvas(frame1, width=photo.width(), height=photo.height(), background="white")
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

#bouton
Button(fen, text ='Niveau précedent').pack(side='left', padx=5, pady=5)
Button(fen, text ='Niveau suivant').pack(side='right', padx=5, pady=5)

#création joueur
player = fct.Joueur(
    vie=3,coord=[920,940],nom_image="image/lighter.gif",canvas=canvas)
player.create()
print(player.obj)

#mouvement du joueur 
canvas.focus_set()
canvas.bind('<Key>', player.mouvement)


#création ennemy


monde_mechant = fct.Monde(canvas=canvas)
monde_mechant.create_monster(lvl=5)


    

#Déplacement ennemy
global dir
dir = 5
def mouv() :
    global liste_enemy,dir
    
    print(canvas.coords(liste_enemy[len(liste_enemy)-1])[2],"cpppr",canvas.winfo_reqwidth())
    if canvas.coords(liste_enemy[len(liste_enemy)-1])[2] > canvas.winfo_reqwidth() -20 :
        dir = -5
        print(dir)
    elif canvas.coords(liste_enemy[0])[2] < 30: 
        dir = 5
    for i in liste_enemy :
        canvas.move(i,dir,0)
    fen.after(50,mouv)

#bouton début de jeu
bouton_jouer = Button(fen, text="Jouer", command=lambda : init_ennemy(5))
bouton_jouer.pack()


#mouvement du canon
"""""
img_canon = PhotoImage ( file = "lighter.gif" )
canon = canvas.create_image(300,300,image =img_canon,anchor="nw")
"""""
#def du canon
global canon
canon = canvas.create_oval(300,290,330,320,fill="yellow")

#a droite du canon
def droite(event) :
    if canvas.coords(canon)[2] < 605 :
        canvas.move(canon,10,0)
    else :
        print("pas bon droite")
canvas.bind_all('<Right>', droite)

#a gauche du canon
def gauche(event) :
    if canvas.coords(canon)[0] >10 :
        canvas.move(canon,-10,0)
    else :
        print("pas bon gauche")
canvas.bind_all('<Left>', gauche)

print(canvas.coords(canon))

#Tire un projectile 
global liste_projectile
liste_projectile =[]
def tir(event) :
    global canon
    xp1 = canvas.coords(canon)[0] +10
    xp2 = canvas.coords(canon)[2] -10
    yp1 = 320
    yp2 = 350
    liste_projectile.append(canvas.create_rectangle(xp1,yp1,xp2,yp2,fill="green"))
canvas.bind_all('<space>', tir)
#mouvement des tirs

def trajectoire() :
    global liste_projectile
    print(liste_projectile)
    for i in liste_projectile :
        
        if canvas.coords(i)[3] > 5 :
            canvas.move(i,0,-10)
            
        else :
            canvas.delete(i) 
            liste_projectile.pop(liste_projectile.index(i))
    fen.after(100,trajectoire)
trajectoire()
fen.mainloop()



