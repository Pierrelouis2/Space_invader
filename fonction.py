import time



class Entity() :
    def __init__(self,vie,coord,forme) :
        self.coord = coord #position de l'entité au début
        self.forme = forme #forme de l'entité
        self.life = vie #vie de l'entité


    def path_monster(self,xmax,ymax,vitesse,dir) : #xmax, ymax limites du canvas #fait droite ou gauche en fonction de dir
            if self.coord[0] + dir*vitesse <= xmax or self.coord[0] + dir*vitesse >= 0 : #déplacement droite
                self.coord[0] += dir*vitesse
                time.sleep(0.5)
                print(self.coord)
                return(dir*vitesse)
        
        
                    






