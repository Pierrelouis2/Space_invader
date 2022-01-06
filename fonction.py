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
        self.player = Joueur(
            vie=3,coord=[920,860],nom_image="image/lighter.gif",canvas=self.canvas)
        self.player.create()



    def jouer(self) :
        print(self.liste_enemy)
        print(self.canvas.find_all())
        for i in self.liste_enemy :
            self.canvas.delete(i.obj)
        self.canvas.delete(self.player.obj)
        self.liste_enemy = []
        self.player = ""
        print("2")
        print(self.liste_enemy)
        print(self.canvas.find_all())






        self.player = Joueur(
            vie=3,coord=[920,860],nom_image="image/lighter.gif",canvas=self.canvas)
        self.player.create()
        
        self.create_monster(lvl=5)




















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
        self.path_monster()
    def path_monster(self,dir=1) :

        print(self.liste_enemy)
        
        if self.canvas.coords(self.liste_enemy[len(self.liste_enemy)-1].obj)[0] > self.canvas.winfo_reqwidth() -20 :
            dir = -1
            
        elif self.canvas.coords(self.liste_enemy[0].obj)[0] < 30: 
            dir = 1
        for i in self.liste_enemy:
            self.canvas.move(i.obj,dir,0)
        self.canvas.after(10,lambda : self.path_monster(dir))