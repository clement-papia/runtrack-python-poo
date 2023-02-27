class Animal:
    def __init__(self):
       self.age = 0
       self.prenom = ""
    def Animal(self):
        self.age = input("Entrez l'age de l'animal:")
        print("l'age de l'animal",self.age,"ans")
    def Vieillir(self):
        somme = int(self.age) + 1
        print("l'age de l'animal",somme,"ans")
    def Nommer(self):
        self.prenom = input("Entrez le nom de l'animal:")
        print ("L'animal se nomme",self.prenom)
        
animal = Animal()
animal.Animal()
animal.Vieillir()
animal.Nommer()