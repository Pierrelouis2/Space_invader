import time
from tkinter.constants import TRUE
from tkinter import *
import random
from tracemalloc import stop



class Entity() :
    def __init__(self,vie,coord,canvas,nom_image) :
        self.coord = coord #position de l'entité au début
        self.life = vie #vie de l'entité
        self.canvas=canvas
        self.nom_image=nom_image
        self.liste_projectile = []
        self.liste_projectile_enemy = []

    def create(self):

        self.photo=PhotoImage(file=self.nom_image)
        self.obj = self.canvas.create_image(self.coord[0],self.coord[1],image=self.photo)
        

class Monstre(Entity):
        def tir_enemy(self) :
            print("ovale")
            xp1 = self.canvas.coords(self.obj)[0] -5
            xp2 = self.canvas.coords(self.obj)[0] +5
            yp1 = self.canvas.coords(self.obj)[1] -7
            yp2 = self.canvas.coords(self.obj)[1] +7
            print(self.canvas.coords(self.obj))
            self.liste_projectile_enemy.append(self.canvas.create_oval(xp1,yp1,xp2,yp2,fill="red"))
            self.traj_tir_enemy()

        def traj_tir_enemy(self) :

            for i in self.liste_projectile_enemy :
    
                if self.canvas.coords(i)[1] < 1200 :
                    self.canvas.move(i,0,10)

                
                else :
                    self.canvas.delete(i) 
                    self.liste_projectile_enemy.remove(i)
            self.canvas.after(100,self.traj_tir_enemy)

            
            

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
                self.liste_projectile.remove(i)
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
        self.dir_enemy_x = 5
        self.dir_enemy_y = 0
        self.lvl =0

        self.var=StringVar()
        self.var.set("Score="+str(self.score))

    def jouer(self) :
        for i in self.liste_enemy :
            self.canvas.delete(i.obj)
        self.liste_enemy =[]
        self.create_monster(lvl=5)

 


    def create_monster(self,lvl) :
        self.lvl = lvl
        
        x = 60
        y = 50
        for i in range(self.lvl) :
            mechant = Monstre(
                vie=1,coord=[x,y],nom_image="image/lighter.gif",canvas=self.canvas)
            mechant.create()
            self.liste_enemy.append(mechant)
            x += 150


        

    def path_monster(self) :
        if len(self.liste_enemy) != 0 :
            self.dir_enemy_y =0
            if self.canvas.coords(self.liste_enemy[len(self.liste_enemy)-1].obj)[0] > self.canvas.winfo_reqwidth() -20 :
                self.dir_enemy_x = -5
                self.dir_enemy_y = 50
                
            elif self.canvas.coords(self.liste_enemy[0].obj)[0] < 30: 
                self.dir_enemy_x = 5
                
            for i in self.liste_enemy:
                if self.canvas.coords(i.obj)[1] > 1200 :
                    print("perdu")
                self.canvas.move(i.obj,self.dir_enemy_x,self.dir_enemy_y)
        
        self.canvas.after(10,self.path_monster)


    def tir_enemy_monde(self) :
        if len(self.liste_enemy) != 0 :
            elu = self.liste_enemy[random.randint(0,len(self.liste_enemy)-1)]
            elu.tir_enemy()
        self.canvas.after(1000,self.tir_enemy_monde)

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
                
    def mort_enemy(self) :
        detruire_enemy = set()
        detruire_proj = set()
        for j in self.liste_enemy:
            for i in self.player.liste_projectile :
                colision_X= self.canvas.coords(j.obj)[0] -20 <= self.canvas.coords(i)[0] <= self.canvas.coords(j.obj)[0] + 20
                colision_Y=self.canvas.coords(j.obj)[1] -20 <= self.canvas.coords(i)[1] <= self.canvas.coords(j.obj)[1] + 20
                if (colision_X == True ) and (colision_Y==True ) :
                    detruire_enemy.add(j)
                    detruire_proj.add(i)
 
        for k in detruire_proj :
            self.canvas.delete(k)
            self.player.liste_projectile.remove(k)
        for t in detruire_enemy :
            self.canvas.delete(t.obj)
            self.liste_enemy.remove(t)
            self.score_fct()
        self.canvas.after(100,self.mort_enemy)
    
    def mort_player(self) :
        detruire_proj_enemy = set()
        for enmy in self.liste_enemy:
            
            for prj  in enmy.liste_projectile_enemy :
                colision_X= self.canvas.coords(self.player.obj)[0] -20 <= self.canvas.coords(prj)[0] <= self.canvas.coords(self.player.obj)[0] + 20
                colision_Y=self.canvas.coords(self.player.obj)[1] -20 <= self.canvas.coords(prj)[1] <= self.canvas.coords(self.player.obj)[1] + 20
                if (colision_X == True ) and (colision_Y==True ) :
                    detruire_proj_enemy.add(prj)
                    self.player.life -= 1
                    print("coucou")

            for k in detruire_proj_enemy :
                self.canvas.delete(k)
                self.enmy.liste_projectile_enemy.remove(k)
        if self.player.life < 0 :
            print("perdu")
        self.canvas.after(100,self.mort_player)


        
        
            
