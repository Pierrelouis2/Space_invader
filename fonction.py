import time
from tkinter.constants import TRUE
from tkinter import *
import random
from tracemalloc import stop

class Entity()   :
    """
    Entity
    Description:
    cree la base de chaque mechant asteroide ou joueur
    """
    def __init__(self,vie,coord,canvas,nom_image) :
        self.coord = coord #position de l'entité au début
        self.life = vie #vie de l'entité
        self.canvas=canvas
        self.nom_image=nom_image
        self.liste_projectile = []
        self.liste_projectile_enemy = []

    def create(self):
        """
        create
        Description:
        cree l entité sur ke canvas
        """
        print("testse",self.nom_image)
        self.photo=PhotoImage(file=self.nom_image)
        self.obj = self.canvas.create_image(self.coord[0],self.coord[1],image=self.photo)
class Monstre(Entity):
    """
    Monstre
    Description:
    Class qui gere les tirs/projectiles des monstres
    """
    def tir_enemy(self) :
        """
        tir_enemy
        Description:
        cree les projectiles
        """
        xp1 = self.canvas.coords(self.obj)[0] -5
        xp2 = self.canvas.coords(self.obj)[0] +5
        yp1 = self.canvas.coords(self.obj)[1] -7
        yp2 = self.canvas.coords(self.obj)[1] +7
        self.liste_projectile_enemy.append(self.canvas.create_oval(xp1,yp1,xp2,yp2,fill="red"))
        
    def traj_tir_enemy(self) :
        """
        traj_tir_enemy
        Description:
        gere la trajectoire des missiles des monstres
        """

        for i in self.liste_projectile_enemy :
            if i != [] :
                if self.canvas.coords(i)[1] < 1200 :
                    self.canvas.move(i,0,10)

                
                else :
                    self.canvas.delete(i) 
                    self.liste_projectile_enemy.remove(i)
        self.canvas.after(50,self.traj_tir_enemy)                    
class Joueur(Entity):
    """
    Joueur
    Description:
    class qui gère le joueur
    """
    def mouvement(self,event) :
        """
        mouvement
        Description:
        deplace le joueur sur le canvas
        """
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

    def tir(self) :
        """
        tir
        Description:
        cree le projectiles du joueur
        """
        
        xp1 = self.canvas.coords(self.obj)[0] +5
        xp2 = self.canvas.coords(self.obj)[0] -5
        yp1 = 828
        yp2 = 842
        self.liste_projectile.append(self.canvas.create_oval(xp1,yp1,xp2,yp2,fill="yellow"))
    
    def trajectoire(self) :
        """
        trajectoire
        Description:
        gere la trajectoire des missiles du joueur
        """
        
        for i in self.liste_projectile :
    
            if self.canvas.coords(i)[3] > 5 :
                self.canvas.move(i,0,-10)
                
            else :
                self.canvas.delete(i) 
                self.liste_projectile.remove(i)
        self.canvas.after(50,self.trajectoire)
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

    def openFile(self):
        """
        openFile
        Description:
        Permet d'ouvrir le fichier texte pour les règles du jeu
        """
        with open('Règle_du_jeu.txt', encoding='utf8') as f:
            for line in f:
                print(line.strip())
            

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
