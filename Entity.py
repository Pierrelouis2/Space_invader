from tkinter import *


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