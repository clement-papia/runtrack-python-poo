class Operation:
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2  
        print("le nombre 1 est",self.nombre1)
        print("le nombre 2 est",self.nombre2)
    
    def addi(self):
        somme = self.nombre1 + self.nombre2
        print(somme)

A = Operation(4,5)
A.addi()