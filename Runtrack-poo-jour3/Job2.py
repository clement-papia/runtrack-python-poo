class CompteBancaire:
    def __init__(self, numérocompte, nomPrenom, solde):
        self.__numérodecompte = numérocompte
        self.__nomprenom= nomPrenom
        self.__solde = solde
        
    def versement(self, argent):
        self.__solde = self.__solde + argent
    
    def retrait(self, argent):
        if(self.__solde < argent):
            print("solde insuffisante")
        else:
            self.__solde = self.__solde - argent
    
    def agios(self):
        self.__solde =self.__solde*95/100
    
    def afficher(self):
        print("Compte numéro : " , self.__numérodecompte)
        print("Nom & Prénom : ", self.__nomprenom)
        print(" Solde  : ", self.__solde)
        print("erreur ")
        
monCompte = CompteBancaire(16168891, " John Dupont", 22300)
monCompte.versement(1500)
monCompte.retrait(24000)
monCompte.agios()
monCompte.afficher()