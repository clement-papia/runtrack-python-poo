class Point:
    def __init__(self,x,y):
        self.cordonnéex = x
        self.cordonnéey = y
    def afficherlespoints(self):
        print("Les cordonnées en x et y sont:",self.cordonnéex,self.cordonnéey)
    def afficherX(self):
        print("Affichage de la cordonnée X:",self.cordonnéex)
    def afficherY(self):
        print("Affichage de la cordonnée Y:",self.cordonnéey)
    def changerX(self, x2):
        self.cordonnéex = x2
        print("La cordonnée X a été changer en",x2)
    def changerY(self,y2):
        self.cordonnéey = y2
        print( "La cordonnée Y a été changer en",y2)

point = Point(5,6)
point.afficherlespoints()
point.afficherX()
point.afficherY()
point.changerX(2)
point.changerY(4)