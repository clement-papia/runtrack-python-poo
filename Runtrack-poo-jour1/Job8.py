class Cercle:
    def __init__(self,rayon,circonférence,air,diametre):
        self.rayon = rayon
        self.circonf = circonférence
        self.air = air
        self.diametre = diametre
    def Changerderayon(self,r2):
        self.rayon = r2
        print("Changement de la valeur du rayon",r2)
    def afficherInfos(self):
        print("Le rayon du cercle est:",self.rayon)
        print("La circonférence du cercle est:",self.circonf)
        print("L'aire du cercle est:",self.air)
        print("Le diamètre du cercle est:",self.diametre) 
    def circonférence(self):
        