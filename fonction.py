import time



class Entity() :
    def __init__(self,vie,coord,forme,canvas) :
        self.coord = coord #position de l'entité au début
        self.forme = forme #forme de l'entité
        self.life = vie #vie de l'entité
        self.canvas=canvas

class Monstre():
    def __init__(self):

        
    def path_monster(self,xmax,ymax,vitesse,dir) : #xmax, ymax limites du canvas #fait droite ou gauche en fonction de dir
        global liste_enemy,dir
    
        print(canvas.coords(liste_enemy[len(liste_enemy)-1])[2],"cpppr",canvas.winfo_reqwidth())
        if canvas.coords(liste_enemy[len(liste_enemy)-1])[2] > canvas.winfo_reqwidth() -20 :
            dir = -5
            print(dir)
        elif canvas.coords(liste_enemy[0])[2] < 30: 
            dir = 5
        for i in liste_enemy :
            canvas.move(i,dir,0)
        fen.after(50,mouv)
        
                    






