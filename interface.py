from tkinter import *
import fonction as fct


fen = Tk()

frame1=Frame(fen)
frame1.pack(side=TOP)

#titre
label = Label(fen, text="Bienvenue dans Space Invader", bg="#d39fce")
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
def init_ennemy(lvl) :
    global liste_enemy,x2,y2
    ligne1 = []
    ligne2=[]
    ligne3=[]
    x1= 5
    x2 = 25
    y1 = 5
    y2 = 25
    liste_enemy = []
    for j in range(3) :
        for i in range(lvl) :

            liste_enemy.append(canvas.create_rectangle(x1,y1,x2,y2,fill="red"))
            x1+= 50
            x2 += 50
            print(x2)
    

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

init_ennemy(8)
mouv()
print(canvas.coords(liste_enemy[0]))
print(canvas.winfo_reqwidth())
fen.mainloop()



