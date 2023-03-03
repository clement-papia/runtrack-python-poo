class LongueurChaine:
    def calculer_longueur(chaine):
        if chaine == "":
            return 0
        else:
            return 1 + LongueurChaine.calculer_longueur(chaine[1:])
  
chaine = input("Entrez une chaîne de caractères : ")
resultat = LongueurChaine.calculer_longueur(chaine)
print("La longueur de la chaîne", chaine, "est", resultat)