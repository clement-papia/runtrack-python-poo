class Ville:
    def __init__(self,nom,nbrhabitants):
       self.__nom = nom
       self.__nbrhabitants = nbrhabitants
    
    def get_Paris(self):
        print("La population de la ville de",self.__nom,"est de",self.__nbrhabitants,"habitants")
    
    def get_Marseille(self):
        print("La population de la ville de",self.__nom,"est de",self.__nbrhabitants,"habitants")

class Personne:
    def __init__(self,nom,age,ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
    
    def ajouterpopulation(self):
            self.__ville += 1
    def get_personne(self):
        print(self.__nom,self.__age,self.__ville)
    
    def set_population(self):
        if self.ajouterpopulation(self):
            self.__ville += 2
            print("Mise à jour de la ville de Paris",self.__ville)

obj = Ville("Paris",1000000)
obj.get_Paris()
obj = Ville("Marseille",861635)
obj.get_Marseille()
obj = Personne("John","45 ans","habitant à Paris")
obj.get_personne()
obj = Personne("Myrtille","4 ans","habitant à Paris")
obj.get_personne()
obj = Personne("Chloé","18 ans","habitant à Marseille")
obj.get_personne()
obj = Personne("John","45 ans","habitant à Paris")
obj.set_population()
