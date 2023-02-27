class Personne:
    def __init__(self,prenom,nom):
        self.prenom = prenom
        self.nom = nom
    def Sepresenter(self):
         print("je m'appelle",self.prenom,self.nom)

personne1 = Personne("John","Doe")
personne1.Sepresenter()
personne2 = Personne("Jean","Dupond")
personne2.Sepresenter()