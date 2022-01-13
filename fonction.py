import time
from tkinter.constants import TRUE
from tkinter import *



class Entity() :
    def __init__(self,vie,coord,canvas,nom_image) :
        self.coord = coord #position de l'entité au début
        self.life = vie #vie de l'entité
        self.canvas=canvas
        self.nom_image=nom_image
        self.liste_projectile = []

    def create(self):

        self.photo=PhotoImage(file=self.nom_image)
        self.obj = self.canvas.create_image(self.coord[0],self.coord[1],image=self.photo)
        

class Monstre(Entity):
        

        pass
                    
class Joueur(Entity):
    def mouvement(self,event) :
        touche = event.keysym
        print(self.obj,"player")
        print(self.canvas.coords(self.obj))
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
    def tir(self) :
        
        xp1 = self.canvas.coords(self.obj)[0] +5
        xp2 = self.canvas.coords(self.obj)[0] -5
        yp1 = 828
        yp2 = 842
        self.liste_projectile.append(self.canvas.create_oval(xp1,yp1,xp2,yp2,fill="yellow"))
        
    
    def trajectoire(self) :
        
        for i in self.liste_projectile :
    
            if self.canvas.coords(i)[3] > 5 :
                self.canvas.move(i,0,-10)
                
            else :
                self.canvas.delete(i) 
                self.liste_projectile.pop(self.liste_projectile.index(i))
        self.canvas.after(100,self.trajectoire)



class Monde () :
    def __init__(self,canvas, texte, mylabel) :
        self.canvas= canvas
        self.texte= texte
        self.label=mylabel
        self.liste_enemy =[]
        self.player = Joueur(
            vie=3,coord=[920,860],nom_image="image/lighter.gif",canvas=self.canvas)
        self.player.create()
        self.score=0
        self.var=StringVar()
        self.var.set("Score="+str(self.score))

    def jouer(self) :
        print(self.liste_enemy)
        print(self.canvas.find_all())
        for i in self.liste_enemy :
            self.canvas.delete(i.obj)
        self.liste_enemy =[]
        
        print("2")
        print(self.liste_enemy)
        
        self.create_monster(lvl=5)
        print(self.canvas.find_all(),'tetet')


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

    def path_monster(self,dir=5) :

        
        if self.canvas.coords(self.liste_enemy[len(self.liste_enemy)-1].obj)[0] > self.canvas.winfo_reqwidth() -20 :
            dir = -5
            
        elif self.canvas.coords(self.liste_enemy[0].obj)[0] < 30: 
            dir = 5
        for i in self.liste_enemy:
            self.canvas.move(i.obj,dir,0)
        self.canvas.after(10,lambda : self.path_monster(dir))

    def mouv(self,event) :
        touche = event.keysym
        if touche == "Right" or touche == "Left" :
            self.player.mouvement(event)
        if touche =="space" :
            self.player.tir()

    def score_fct(self):
        self.score+=50
        self.texte.set("Bienvenue dans Space Invader                                                                  Score : "+str(self.score))
        print(self.score)
        self.label.configure(text=self.texte.get())

    def mort(self) :
        self.detruire_enemy = set()
        self.detruire_proj = set()
        for j in self.liste_enemy:
            for i in self.player.liste_projectile :
                colision_X= self.canvas.coords(j.obj)[0] -20 <= self.canvas.coords(i)[0] <= self.canvas.coords(j.obj)[0] + 20
                colision_Y=self.canvas.coords(j.obj)[1] -20 <= self.canvas.coords(i)[1] <= self.canvas.coords(j.obj)[1] + 20
                if (colision_X == True ) and (colision_Y==True ) :
                    self.detruire_enemy.add(j)
                    self.detruire_proj.add(i)
                    print("touche")
        for k in self.detruire_proj :
            self.canvas.delete(k)
            self.player.liste_projectile.remove(k)
        for t in self.detruire_enemy :
            self.canvas.delete(t.obj)
            self.liste_enemy.remove(t)
            self.score_fct()
        
        self.canvas.after(100,self.mort)


                
    