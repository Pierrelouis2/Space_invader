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
        print("test create")
        self.photo=PhotoImage(file=self.nom_image)
        self.obj = self.canvas.create_image(self.coord[0],self.coord[1],image=self.photo)
        

class Monstre(Entity):
  
        

        pass
                    
class Joueur(Entity):
    def mouvement(self,event) :
        touche = event.keysym
        if touche == "Right" :
            
            if self.canvas.coords(self.obj)[0] < 1880 :
                self.canvas.move(self.obj,10,0)
            else :
                print("pas bon droite")
        if touche == "Left" :
            if self.canvas.coords(self.obj)[0] >40 :
                    self.canvas.move(self.obj,-10,0)
            else :
                print("pas bon gauche")
#    canvas.bind_all('<Left>', gauche)
 



class Monde () :
    def __init__(self,canvas) :
        self.canvas= canvas
        self.liste_enemy =[]
    def create_monster(self,lvl) :
        self.lvl = lvl
        
        x = 60
        y = 50
        print("test1")
        for i in range(self.lvl) :
            print("test2")
            mechant = Monstre(
                vie=1,coord=[x,y],nom_image="image/lighter.gif",canvas=self.canvas)
            mechant.create()
            self.liste_enemy.append(mechant)
            x += 150
            print(self.liste_enemy,"testestest")
        self.path_monster(5)

    def path_monster(self,dir) :

        print(self.canvas.coords(self.liste_enemy[0].obj),'testte')
        
        if self.canvas.coords(self.liste_enemy[len(self.liste_enemy)-1].obj)[0] > self.canvas.winfo_reqwidth() -20 :
            dir = -5
            print(dir)
        elif self.canvas.coords(self.liste_enemy[0].obj)[0] < 30: 
            dir = 5
        for i in self.liste_enemy :
            self.canvas.move(i,dir,0)
        self.canvas.after(50,lambda : self.path_monster(dir,self.liste_enemy))