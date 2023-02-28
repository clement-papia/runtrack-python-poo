class Livre:
    def __init__(self,titre,auteur,nbrpages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbrpages = nbrpages
    
    def get_titre(self):
        print("la titre est ",self.__titre)
    
    def get_auteur(self):
        print("l'auteur de ce livre est",self.__auteur)
    
    def get_nbrpages(self):
        print("le nombre de pages est de",self.__nbrpages)

    def set_titre(self, titre):
        self.__titre = titre
        print("Nouveau titre",self.__titre)

    def set_auteur(self, auteur):
        self.__auteur = auteur
        print("Nouveau auteur",self.__auteur)

    def set_nbrpages(self, nbrpages):
        if nbrpages<0:
            print("erreur")
        else:
            self.__nbrpages = nbrpages
            print("le nombre de pages est de",self.__nbrpages)

livre = Livre("Le petit prince","Antoine de Saint-Exupéry",93)
livre.get_titre()
livre.get_auteur()
livre.get_nbrpages()
livre.set_titre("Harry potter")
livre.set_auteur("J. K. Rowling")
livre.set_nbrpages(-1)