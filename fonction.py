import time
from tkinter.constants import TRUE
from tkinter import *



class Entity() :
    def __init__(self,vie,coord,canvas,nom_image) :
        self.coord = coord #position de l'entité au début
        self.life = vie #vie de l'entité
        self.canvas=canvas
        self.nom_image=nom_image

    def create(self):
        self.photo=PhotoImage(file=self.nom_image)
        self.obj = self.canvas.create_image(self.coord[0],self.coord[1],image=self.photo)
        

class Monstre(Entity):
    def __init__(self):

        pass
    def path_monster(self,xmax,ymax,vitesse,dir) : #xmax, ymax limites du canvas #fait droite ou gauche en fonction de dir
        
    
        print(self.canvas.coords(self.liste_enemy[len(self.liste_enemy)-1])[2],"cpppr",self.canvas.winfo_reqwidth())
        if self.canvas.coords(self.liste_enemy[len(self.liste_enemy)-1])[2] > self.canvas.winfo_reqwidth() -20 :
            dir = -5
            print(dir)
        elif self.canvas.coords(self.liste_enemy[0])[2] < 30: 
            dir = 5
        for i in self.liste_enemy :
            self.canvas.move(i,dir,0)
        fen.after(50,mouv)
        
                    
class Joueur(Entity):

 

    pass


