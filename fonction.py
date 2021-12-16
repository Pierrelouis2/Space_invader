import time



class Entity() :
    def __init__(self,vie,pos,forme) :
        self.pos = pos #position de l'entité au début
        self.forme = forme #forme de l'entité
        self.life = vie #vie de l'entité


    def path_monster(self,xmax,ymax,vitesse) : #xmax, ymax limites du canvas
        if self.pos[0] == 0 :
            while self.pos[0] != xmax :
                if int(self.pos[0]) + vitesse <= int(xmax) : #déplacement droite
                    self.pos[0] += vitesse
                    time.sleep(1)
                    print(self.pos)
        elif self.pos[0] == xmax :
            while self.pos[0] != 0 :
                if int(self.pos[0]) - int(vitesse) >= 0 : #déplacement gauche
                    self.pos[0] -= vitesse
                    time.sleep(1)
                    print(self.pos)
            
                    
entity1 = Entity(1,[0,0],1)

while 2 !=3 :
    entity1.path_monster(100,200,10)




