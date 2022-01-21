
from tkinter import *
import random
from Joueur import *
from Monstre import *


                    

class Monde () :
    """
    Monde
    Description:
    Class qui englobe tout
    """
    def __init__(self,canvas, texte) :
        self.canvas= canvas
        self.texte= texte
        self.liste_enemy =[]
        self.player = Joueur(
            vie=3,coord=[920,860],nom_image="image/lighter.gif",canvas=self.canvas)
        self.player.create()
        self.score=0
        self.dir_enemy_x = 5
        self.dir_enemy_y = 0
        self.lvl =5
        self.liste_asteroid = []
        self.passe = False
        self.var=StringVar()
        self.var.set("Score="+str(self.score))

    

    def createNewWindow(self):
        """
        createNewWindow
        Description:
        Permet d'ouvrir le fichier texte pour les règles du jeu
        """
        with open("Règle_du_jeu.txt") as file:
            content = file.read()
        newWindow = Toplevel()
        labelExample = Label(newWindow, text = content)

        labelExample.pack()
        
            

    def jouer(self) :
        """
        jouer
        Description:
        permet de remettre a 0 le jeu
        """
        print("jouer")
        for i in self.liste_enemy :
            for k in i.liste_projectile_enemy :
                self.canvas.delete(k)
            self.canvas.delete
            self.canvas.delete(i.obj)
        self.liste_enemy =[]
        self.lvl=1
        self.create_monster(lvl=self.lvl)

        for i in self.liste_asteroid :
            self.canvas.delete(i)
        self.liste_asteroid=[]
        self.create_asteroid()
        self.score = 0
        self.player.life = 3
        self.score_fct()
        self.passe = True
    def niveau(self) :
        """
        niveau
        Description:
        augmente la difficulté de 1 quand tous les mechant sont morts
        """
        if self.passe == True :
            if self.liste_enemy == [] :
                self.lvl +=1
                self.create_monster(lvl=self.lvl)
        self.canvas.after(10,self.niveau)

    def create_monster(self,lvl) :
        """
        create_monster
        Description:
        cree les mechant en fonction du niveau/difficulté
        """
        self.lvl = lvl
        x = 60
        y = 50
        if self.lvl == 10 :
            print("lvl 10")
            x =900
            y = 100
            bonus = Monstre(
                vie=25,coord=[x,y],nom_image="image/bonussok.png",canvas=self.canvas)
            bonus.create()
            bonus.traj_tir_enemy()
            self.liste_enemy.append(bonus)
            self.lvl = 1
        else :
            for i in range(self.lvl) :
                mechant = Monstre(
                    vie=1,coord=[x,y],nom_image="image/alien_transparent.png",canvas=self.canvas)
                mechant.create()
                mechant.traj_tir_enemy()
                self.liste_enemy.append(mechant)
                x += 150

    def path_monster(self) :
        """
        path_monster
        Description:
        gere la trajectoire des mechants
        """
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
        """
        tir_enemy_monde
        Description:
        tir aleatoir des enemy
        """
        if len(self.liste_enemy) != 0 :
            elu = self.liste_enemy[random.randint(0,len(self.liste_enemy)-1)]
            elu.tir_enemy()
        self.canvas.after(1000,self.tir_enemy_monde)

    def mouv(self,event) :
        """
        mouv
        Description:
        Gere le mouvement du joueur
        """
        touche = event.keysym
        if touche == "Right" or touche == "Left" :
            self.player.mouvement(event)
        if touche =="space" :
            self.player.tir()
            
    def score_fct(self):
        """
        score_fct
        Description:
        affiche le score et la vie du joueur
        """
        self.texte.set("Bienvenue dans Space Invader                              Vie : " +str(self.player.life)+"                                              Score : "+str(self.score))
                
    def mort_enemy(self) :
        """
        mort_enemy
        Description:
        Regarde si un enemy est touche ou pas
        """
        detruire_enemy = set()
        detruire_proj = set()
        for j in self.liste_enemy:
            for i in self.player.liste_projectile :
                colision_X= self.canvas.coords(j.obj)[0] -60 <= self.canvas.coords(i)[0] <= self.canvas.coords(j.obj)[0] + 60
                colision_Y= self.canvas.coords(j.obj)[1] - 50 <= self.canvas.coords(i)[1] <= self.canvas.coords(j.obj)[1] + 50
                if (colision_X == True ) and (colision_Y==True ) :
                    j.life -= 1
                    detruire_proj.add(i)
                    if j.life == 0 :
                        detruire_enemy.add(j)
                        
 
        for k in detruire_proj :
            self.canvas.delete(k)
            self.player.liste_projectile.remove(k)
        
        for t in detruire_enemy :
            for l in t.liste_projectile_enemy :
                self.canvas.delete(l)
            self.canvas.delete(t.obj)
            self.liste_enemy.remove(t)
            if t.coord[0] == 900 :
                self.score+=100
                self.score_fct()
            else : 
                self.score+=50
                self.score_fct()
        self.canvas.after(100,self.mort_enemy)
    
    def mort_player(self) :
        """
        mort_player
        Description:
        regarde si le joueur se fait touche
        """
        for enmy in self.liste_enemy:
            detruire_proj_enemy = set()
            for prj  in enmy.liste_projectile_enemy :
                colision_X= self.canvas.coords(self.player.obj)[0] -30 <= self.canvas.coords(prj)[0] <= self.canvas.coords(self.player.obj)[0] + 30
                colision_Y=self.canvas.coords(self.player.obj)[1] -20 <= self.canvas.coords(prj)[1] <= self.canvas.coords(self.player.obj)[1] +20
                if colision_X and colision_Y :
                    detruire_proj_enemy.add(prj)
                    self.player.life -= 1
                    self.score_fct()


            for k in detruire_proj_enemy :
                self.canvas.delete(k)
                enmy.liste_projectile_enemy.remove(k)

        if self.player.life == 0 :
            self.canvas.delete(self.player.obj)
            self.player= ''
            for i in self.liste_enemy :
                for k in i.liste_projectile_enemy :
                    self.canvas.delete(k)
            self.canvas.delete(i.obj)
            self.liste_enemy =[]
            for i in self.liste_asteroid :
                self.canvas.delete(i)
            self.liste_asteroid=[]
        self.canvas.after(100,self.mort_player)

    def create_asteroid(self) :
        """
        create_asteroid
        Description:
        crée les asteroides
        """
        x = 300
        y = 600

        for i in range(4) :
            asteroid= Monstre(
                vie=10,coord=[x,y],nom_image="image/meteor.gif",canvas=self.canvas)
            asteroid.create()
            self.liste_asteroid.append(asteroid)
            x +=400
    
    def col_asteroid(self) :
        """
        col_asteroid
        Description:
        regarde si un asteroid se fait touche
        """
        detruire_proj_player = set()
        for j in self.liste_asteroid :
            for i in self.player.liste_projectile :
                    colision_X= self.canvas.coords(j.obj)[0] -120 <= self.canvas.coords(i)[0] <= self.canvas.coords(j.obj)[0] + 90
                    colision_Y= self.canvas.coords(i)[1] <= self.canvas.coords(j.obj)[1] + 60
                    if (colision_X == True ) and (colision_Y==True ) :
                        j.life -=1
                        detruire_proj_player.add(i)

            for enmy in self.liste_enemy:
                detruire_proj_enemy = set()
                
                for prj  in enmy.liste_projectile_enemy :
                    colision_X= self.canvas.coords(j.obj)[0] -120 <= self.canvas.coords(prj)[0] <= self.canvas.coords(j.obj)[0] + 90
                    colision_Y=self.canvas.coords(j.obj)[1] -100 <= self.canvas.coords(prj)[1] 
                    if colision_X and colision_Y :
                        detruire_proj_enemy.add(prj)
                        j.life -=1
                for p in detruire_proj_enemy :  
                    self.canvas.delete(p)
                    enmy.liste_projectile_enemy.remove(p)
         
            if j.life == 0 : 
                self.canvas.delete(j.obj)
                self.liste_asteroid.remove(j)



        for k in detruire_proj_player :
            self.canvas.delete(k)
            self.player.liste_projectile.remove(k)

        self.canvas.after(50,self.col_asteroid)
