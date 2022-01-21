from tkinter import *
from Entity import *


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