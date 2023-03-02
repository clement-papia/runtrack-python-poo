class Student:
    def __init__(self,prenom,nom,numéroétudiant,nombredecrédit = 0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numéroétudiant = numéroétudiant
        self.__nombredecrédit = nombredecrédit
    
    def add_credits(self,credits):
        if credits>0:
            self.__nombredecrédit += credits
            print("Le nombre de credits de John Doe est de",credits)
        
eleve = Student("John","Doe",145)
eleve.add_credits(60)