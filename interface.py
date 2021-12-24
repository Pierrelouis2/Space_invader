from tkinter import *
import fonction as fct


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
photo = PhotoImage(file="backgroundimage.png")
canvas = Canvas(frame1, width=photo.width(), height=photo.height(), background="white")
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

#bouton
Button(fen, text ='Niveau précedent').pack(side='left', padx=5, pady=5)
Button(fen, text ='Niveau suivant').pack(side='right', padx=5, pady=5)


#création ennemy
global liste_enemy 
global mouv_pass
mouv_pass = 1
liste_enemy = []
def init_ennemy(lvl) :
    global liste_enemy, x2,y2,mouv_pass
    for k in liste_enemy :
        canvas.delete(k)#penser a reset les ennemy du canvas
    ligne1 = []
    ligne2=[]
    ligne3=[]
    x1= 5
    x2 = 25
    y1 = 5
    y2 = 25
    liste_enemy = []
    
    for i in range(lvl) :

        liste_enemy.append(canvas.create_rectangle(x1,y1,x2,y2,fill="red"))
        x1+= 50
        x2 += 50
        print(x2)
    if mouv_pass == 1 :
        mouv()
        mouv_pass = 0

#Déplacement ennemy
global dir
dir = 5
def mouv() :
    global liste_enemy,dir
    
    print(canvas.coords(liste_enemy[len(liste_enemy)-1])[2],"cpppr",canvas.winfo_reqwidth())
    if canvas.coords(liste_enemy[len(liste_enemy)-1])[2] > canvas.winfo_reqwidth() :
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

#def du canon
"""""
img_canon = PhotoImage ( file = "lighter.gif" )
canon = canvas.create_image(300,300,image =img_canon,anchor="nw")
"""""
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

fen.mainloop()



