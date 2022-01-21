from tkinter import *
from Entity import *

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