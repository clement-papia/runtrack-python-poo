class Personnage:
    def __init__(self):
        self.x = 0
        self.y = 0
    def gauche(self):
        somme = int(self.x) -1
        print("Le personnage se déplace à gauche de",somme)
    def droite(self):
        somme = int(self.x) +1
        print("Le personnage se déplace à droite de",somme)
    def bas(self):
       somme = int(self.y) + 1
       print("Le personnage se déplace en bas de",somme)
    def haut(self):
       somme = int(self.y) -1
       print("Le personnage se déplace en haut de",somme)
    def position(self):
        pose = (self.x,self.y)
        print("Voici les coordonnées en x et y",pose)

personnage = Personnage()
personnage.gauche()
personnage.droite()
personnage.bas()
personnage.haut()
personnage.position()