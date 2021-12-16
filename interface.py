from tkinter import *
fenetre = Tk()

class alien():
    def __init__(self,fen) :   
        self.canvas = Canvas(fen)
        self.posx = []
        self.ent = fct.Entity(1,[0,0],1)
        self.rectangle = self.canvas.create_rectangle(5,5,25,25,fill='black')
        self.canvas.pack()
    def mouvement(self,dir) :
        self.posx = self.ent.path_monster(700,500,10,dir)
        self.canvas.move(self.rectangle,self.posx,0)




alien1=alien(fenetre)






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



