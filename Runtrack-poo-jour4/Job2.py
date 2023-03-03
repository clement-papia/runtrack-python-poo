class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("L'âge de la personne est", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=30):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

    def getMatiereEnseignee(self):
        return self.__matiereEnseignee

    def setMatiereEnseignee(self, nouvelleMatiere):
        self.__matiereEnseignee = nouvelleMatiere
        
p = Personne()
e = Eleve()
print("L'âge par défaut de l'élève est", e.age)
e.modifierAge(15)
e.bonjour()
e.allerEnCours()
e.modifierAge(15)
e.afficherAge()
p = Professeur("mathématiques", 40)
p.bonjour()
p.enseigner()