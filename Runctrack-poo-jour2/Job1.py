class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def get_longueur(self):
        print("la longueur du rectangle est de",self.__longueur)
    
    def get_largeur(self):
        print("la largueur du rectangle est de",self.__largeur)

    def set_longueur(self, nombre):
        self.__longueur = nombre
        print("la nouvelle longueur est",self.__longueur)
    
    def set_largeur(self, nombre):
        self.__largeur = nombre
        print("la nouvelle largeur est",self.__largeur)          

rectangle = Rectangle(5,10)
rectangle.get_longueur()
rectangle.get_largeur()
rectangle.set_longueur(5)
rectangle.set_largeur(6)