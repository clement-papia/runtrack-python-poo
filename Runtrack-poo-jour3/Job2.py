class CompteBancaire:
    def __init__(self,numérocompte, nom, prénom,solde):
        self.__numérocompte = numérocompte
        self.__nom = nom
        self.__prénom = prénom
        self.__solde = solde
    
    def afficher(self):
        print("Voici les informations de votre compte",self.__numérocompte)
    
    def afficherSolde(self):
        print("Voici vos soldes",self.__solde)
    
    def versement(self,montant):
        if self.__solde > montant:
            self.__solde += montant
            print("voici votre nouveau montant",self.__solde)
    
    def retrait(self,montant):
        if self.__solde > montant:
            self.__solde -= montant
            print("voici votre nouveau montant",self.__solde)
        else:
            self.__solde < 0
            print("Vous ne possèdez pas le montant disponible")
    
    