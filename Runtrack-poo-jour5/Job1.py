class Factorielle:
    def calculer_fact(n):
        if n == 0:
            return 1
        else:
            return n * Factorielle.calculer_fact(n - 1)
  
nombre_entier = int(input("Entrez un nombre entier : "))
resultat = Factorielle.calculer_fact(nombre_entier)
print("La factorielle de", nombre_entier, "est", resultat)